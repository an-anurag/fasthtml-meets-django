import os
import django
from blog.models import Author, Post, Comment

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Create an author
author = Author.objects.create(name="John Doe", email="johndoe@example.com")

# Create a post
post = Post.objects.create(
    title="My First Post",
    content="This is the content of my first post.",
    status="published",
    author=author
)

# Create a comment
comment = Comment.objects.create(
    post=post,
    name="Jane Smith",
    email="janesmith@example.com",
    content="Great post!"
)

print("Data inserted successfully!")
