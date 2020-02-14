import os
import django

#for accesing the models these lines mandatory.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_blog.settings')
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from blog.models import Post
from users.models import Profile
import random


#creting the users
# def creating_users_data(n=None):
#     fake = Faker()
#     for entry in range(n):
#         username = fake.first_name()
#         email   = fake.email()
#         password1 = 'testuser123' 
#         user = User.objects.create(username = username,
#                 email = email,
#                 password = password1,
    
#             )

# if __name__ == "__main__":
#     print("Users data is opulating please wait..........")
#     creating_users_data(10)
#     print("data population is completed !!!!!")


# creating posts
def create_posts(n=None):
    fake = Faker()
    users = User.objects.all()
    for entry in range(n):
        title = fake.sentence()
        content  = fake.text()*5
        user = random.choice(users)

        Post.objects.create(title = title,
                content = content,
                author = user,
    
            )

if __name__ == "__main__":
    print("Posts data is populating please wait..........")
    create_posts(100)
    print("data population is completed !!!!!")



 




