from api_wrappers import VkWrapper

def main():
    Vk=VkWrapper.VkWrapper()
    print (Vk.get_User_info())



if __name__=="__main__":
    main()