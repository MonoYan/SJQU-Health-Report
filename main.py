import os
from GenchAPI import GenchAPI
GenchAPI.sign(os.environ.get('username') , os.environ.get('password'), 0, "上海市", "上海市", "虹口区")
