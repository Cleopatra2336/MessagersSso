import requests
import libs.main_configs as main_configs


class VkWrapper(object):
    def __init__(self):
        self.auth_token=main_configs.TOKEN



    def get_User_info(self):
        r = requests.get("https://api.vk.com/method/users.get?user_id=210700286&v=5.52")
        print (r.json())








def main():
    return


if __name__=="__main__":
    main()