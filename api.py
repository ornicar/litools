import requests
import json
from collections import defaultdict
import time
from datetime import datetime
from dateutil import tz
from threading import Lock


class RequestType:
    def __init__(self, name, delay=1.0, num_requests=1):
        self.name = name
        self.delay = delay
        self.num_requests = num_requests


class ApiType:
    # Get
    ApiAccount = RequestType('api/account')
    ApiUser = RequestType('api/user')
    ApiUserNote = RequestType('api/user/note')
    ApiUserModLog = RequestType('api/user/mod-log')
    ApiUsersStatus = RequestType('api/users/status')
    ReportListBoost = RequestType('report/list/boost')
    ApiTeamOf = RequestType('api/team/of')
    AtUsernameFollowing = RequestType('@/username/following')
    ApiTournamentId = RequestType('api/tournament/id')
    ApiSwiss = RequestType('api/swiss')
    ApiTournament = RequestType('api/tournament')
    TournamentId = RequestType('tournament')
    SwissId = RequestType('swiss')
    BroadcastId = RequestType('broadcast')
    PlayerTop = RequestType('player/top')
    # Get ndjson
    ApiGamesUser = RequestType('api/games/user')
    ApiTeamArena = RequestType('api/team/arena')
    ApiTeamSwiss = RequestType('api/team/swiss')
    ApiBroadcast = RequestType('api/broadcast')
    ApiTournamentResults = RequestType('api/tournament/results')
    ApiSwissResults = RequestType('api/swiss/results')
    # Post
    ApiUserNote_Post = RequestType('api/user/note:post')
    ApiWarn = RequestType('api/warn')
    ApiBooster = RequestType('api/booster')
    InsightsRefresh = RequestType('insights/refresh', 60, 4)
    InsightsData = RequestType('insights/data')
    ModPublicChatTimeout = RequestType('mod/public-chat/timeout')
    ModWarn = RequestType('mod/warn')
    ModKid = RequestType('mod/kid')
    ModTroll = RequestType('mod/troll')
    ApiUsers = RequestType('api/users')
    # Delete
    ApiToken_Delete = RequestType('api/token:delete')


class Api:
    ndjson_lock = Lock()
    verbose = 0  # 0, 1, 2

    def __init__(self):
        self.api_times = defaultdict(list)

    def wait(self, api: RequestType):
        now = datetime.now()
        wait_s = 0
        if len(self.api_times[api.name]) >= api.num_requests:
            wait_s = api.delay - (now - self.api_times[api.name][-api.num_requests]).total_seconds()
        self.api_times[api.name].append(now)
        if len(self.api_times[api.name]) > api.num_requests:
            self.api_times[api.name] = self.api_times[api.name][-api.num_requests:]
        if wait_s > 0:
            if Api.verbose >= 2:
                print(f'Waiting for "{api.name}" for {wait_s:0.1f}s')
            time.sleep(wait_s)

    def get_waiting_time(self, api: RequestType):
        now = datetime.now()
        if len(self.api_times[api.name]) >= api.num_requests:
            return api.delay - (now - self.api_times[api.name][-api.num_requests]).total_seconds()
        return 0

    def prepare(self, api: RequestType, url, token, tag, **kwargs):
        if Api.verbose:
            print(f"request {datetime.now(tz=tz.tzutc()):%H:%M:%S.%f}: {tag} {url}")
        self.wait(api)
        if token is None:
            headers = kwargs.pop('headers', None)
        else:
            headers = kwargs.pop('headers', {}).copy()
            headers['Authorization'] = f"Bearer {token}"
        return headers

    def get(self, api_type: RequestType, url, token=None, **kwargs):
        headers = self.prepare(api_type, url, token, "GET", **kwargs)
        kwargs.pop('headers', None)
        r = requests.get(url, headers=headers, **kwargs)
        if r.status_code == 429:
            print(f"ERROR: Status 429: {datetime.now(tz=tz.tzutc()):%Y-%m-%d %H:%M:%S.%f} GET: {url}")
            time.sleep(60)
        return r

    def post(self, api_type: RequestType, url, token=None, **kwargs):
        headers = self.prepare(api_type, url, token, "POST", **kwargs)
        kwargs.pop('headers', None)
        r = requests.post(url, headers=headers, **kwargs)
        if r.status_code == 429:
            print(f"ERROR: Status 429: {datetime.now(tz=tz.tzutc()):%Y-%m-%d %H:%M:%S.%f} POST: {url}")
            time.sleep(60)
        return r

    def delete(self, api_type: RequestType, url, token=None, **kwargs):
        headers = self.prepare(api_type, url, token, "DELETE", **kwargs)
        kwargs.pop('headers', None)
        r = requests.delete(url, headers=headers, **kwargs)
        if r.status_code == 429:
            print(f"ERROR: Status 429: {datetime.now(tz=tz.tzutc()):%Y-%m-%d %H:%M:%S.%f} DELETE: {url}")
            time.sleep(60)
        return r

    def get_ndjson(self, api_type, url, token, Accept="application/x-ndjson"):
        if Api.verbose:
            print(f"request {datetime.now(tz=tz.tzutc()):%H:%M:%S.%f}: {url}")
        self.wait(api_type)
        headers = {'Accept': Accept,
                   'Authorization': f"Bearer {token}"}
        with Api.ndjson_lock:
            r = requests.get(url, allow_redirects=True, headers=headers)
            if r.status_code == 429:
                if Api.verbose:
                    print(f"waiting 60s...request {datetime.now():%H:%M:%S.%f} {api_type}")
                time.sleep(60)
        if Api.verbose >= 2:
            print(f"finish {datetime.now(tz=tz.tzutc()):%H:%M:%S.%f}: {url}")
        if r.status_code != 200:
            try:
                i1 = url.find(".org/")
                i2 = url.rfind("/")
                api = url[i1 + 4:i2 + 1]
            except:
                api = url
            raise Exception(f"{api}: Status code = {r.status_code}")
        content = r.content.decode("utf-8")
        lines = content.split("\n")[:-1]
        data = [json.loads(line) for line in lines]
        return data
