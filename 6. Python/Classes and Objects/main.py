from user import User
from post import Post

user_one = User("aa@aa.com", "sudheer", "pwd1", "Agent")
user_one.get_user_info()

user_two = User("bb@aa.com", "Supreet", "pwd2", "Manager")
user_two.get_user_info()

new_post = Post("Devops Concepts", user_two.name)
new_post.get_post_info()
