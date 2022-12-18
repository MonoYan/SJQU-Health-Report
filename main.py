import os
from GenchAPI import GenchAPI
GenchAPI.sign(os.environ.get('username') , os.environ.get('password'), 0, "内蒙古自治区", "呼伦贝尔市", "海拉尔区")
