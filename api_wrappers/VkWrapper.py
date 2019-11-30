import requests
from libs import vk_congigs


class VkWrapper(object):
    def __init__(self):
        self.auth_token=vk_congigs.TOKEN



    def get_User_info(self):
        r = requests.get("https://api.vk.com/method/users.get?user_id=210700286&v=5.52")
        return r.json()