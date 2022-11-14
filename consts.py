# Chat
CHAT_TOURNAMENT_FINISHED_AGO = 12 * 60  # [min]
CHAT_TOURNAMENT_STARTS_IN = 6 * 60  # [min]
CHAT_SWISS_STARTED_AGO = 6 * 60  # [min]
MAX_LEN_TOURNEY_NAME_SHORT = 25
MAX_LEN_TOURNEY_NAME_LONG = 33
NUM_RECENT_BROADCASTS_TO_FETCH = 20

API_TOURNEY_PAGE_DELAY = 1.0  # [s]
IDX_NO_PAGE_UPDATE = 0
API_CHAT_REFRESH_PERIOD = [1, 5, 25, 60]  # [s]
PERIOD_UPDATE_TOURNAMENTS = 60  # [s]
TIME_FREQUENT_MESSAGES = 5  # [s]
MAX_TIME_FREQUENT_MESSAGES = 60  # [s]
NUM_FREQUENT_MESSAGES = 9
NUM_MSGS_BEFORE = 10
NUM_MSGS_AFTER = 10
TIMEOUT_RANGE = [25, 25]  # [min]
DELAY_ERROR_READ_MOD_LOG = 60  # [min]
DELAY_ERROR_CHAT_404 = 10 * 60   # [s]
TIME_CHAT_REMOVED_404 = 30 * 60   # [s]
RECENT_TIMEOUT = 12 * 60 * 60  # [s]
RECENT_WARNING = 7 * 24 * 60 * 60  # [s]
LIFETIME_USER_CACHE = 1 * 60 * 60  # [s]

CHAT_NUM_VISIBLE_MSGS = 450
CHAT_MAX_NUM_MSGS = 500
CHAT_FREQUENT_MSGS_MIN_SCORE = [15, 30]
CHAT_BEGINNING_MESSAGES_TEXT = '"name":"Chat room","lines":['
CHAT_END_MESSAGES_TEXT = '],"userId":'
TOURNEY_STANDING_BEGINNING_TEXT = '"standing":{"page":1,"players":['
TOURNEY_STANDING_ENDING_TEXT = ']},"socketVersion":'
HR = '<hr class="my-0" style="border-top:dotted 2px;"/>'
CHAT_UPDATE_SWISS = False  # loading messages from swiss tourneys doesn't work at the moment anyway
DO_AUTO_TIMEOUTS = False
MULTI_MSG_MIN_TIMEOUT_SCORE = 300
MAX_LEN_TEXT = 140
CHAT_NUM_PLAYED_GAMES = [100, 250]
CHAT_CREATED_DAYS_AGO = [30, 60]
STD_SHORT_MESSAGES = ["hi", "hello", "good luck", "bye", "gl", "hf", "thanks", "gg", "wp", "ggs", "ty", "gtg", "thx", "u2"]


# Boost
BOOST_UPDATE_PERIOD = 5 * 60  # seconds

BOOST_SUS_PROGRESS = 50
BOOST_SUS_NUM_GAMES = 50
BOOST_SUS_RATING_DIFF = [150, 300]
BOOST_NUM_GAMES = [100, 200, 500]
BOOST_NUM_MOVES = [0, 5, 10, 15]
BOOST_BAD_GAME_PERCENT = {0: [0.05, 0.10], 5: [0.08, 0.15], 10: [0.10, 0.20], 15: [0.15, 0.33]}
BOOST_STREAK_TIME = 10 * 60  # interval between games [s]
BOOST_STREAK_REPORTABLE = 3
BOOST_NUM_RESIGN_REPORTABLE = 3
BOOST_NUM_TIMEOUT_REPORTABLE = 3
BOOST_NUM_OUT_OF_TIME_REPORTABLE = 3
BOOST_SIGNIFICANT_RATING_DIFF = 150
BOOST_SUS_STREAK = 3
BOOST_NUM_PLAYED_GAMES = [100, 250]
BOOST_CREATED_DAYS_AGO = [30, 60]
BOOST_ANALYSIS_SCORE = 2
BOOST_NUM_GAMES_FREQUENT_OPP = 4
BOOST_PERCENT_FREQUENT_OPP = 0.30
BOOST_MIN_DECENT_RATING = 1500  # TODO: different for different variants
NUM_FIRST_GAMES_TO_EXCLUDE = 15
MAX_NUM_TOURNEY_PLAYERS = 20
STD_NUM_TOURNEYS = 5
MIN_NUM_TOURNEY_GAMES = 4
MAX_LEN_TOURNEY_NAME = 22
API_TOURNEY_DELAY = 0.5  # [s]
BOOST_RING_TOOL = b'iSfVR3ICd3lHqSQf2ucEkLvyvCf0'
STATUSES_TO_DISCARD_BOOST = ["created", "started", "aborted", "unknownFinish", "draw", "cheat"]
PERCENT_EXTRA_GAMES_TO_DOWNLOAD = 10

# Alt
MAX_NUM_GAMES_TO_DOWNLOAD = 99999
STATUSES_TO_DISCARD_ALT = ["created", "started", "aborted", "unknownFinish"]
NUM_EXAMPLE_GAMES = 5
ALT_SWITCH_INTERVAL_MINS = [0, 5, 20, 60, 3*60, 12*60, 24*60, 7*24*60]
ALT_SWITCH_INTERVAL_NAMES = ["In parallel", "<5 min", "<20 min", "<1 h", "<3 h", "<12 h", "<1 day", "<1 week", "1+ weeks"]
ALT_MAX_NUM_TCS_TO_SHOW = 8
ALT_MAX_NUM_OPENINGS_TO_SHOW = 8
ALT_MAX_LEN_NAME = 8
CHART_WIDTH = 1000
BAR_DANGER = 'rgba(231, 76, 60, 1)'
ALT_UPDATE_PERIOD = 30 * 60  # seconds
ALT_REFRESH_OPENINGS_PERIOD = 24 * 60 * 60  # seconds
ALT_MAX_PERIOD_FOR_GAMES = 2*365  # days
