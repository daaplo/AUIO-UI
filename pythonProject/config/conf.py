import os
base_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(base_dir, 'logs')
allure_img_dir = os.path.join(base_dir, 'img_allure')
if __name__== '__main__':
    print(base_dir)
    print(allure_img_dir)
    print(log_dir)