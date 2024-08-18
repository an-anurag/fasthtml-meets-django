from fasthtml.common import *
from blog.models import Post, Comment

app, rt = fast_app(debug=True, live=True)


def post_list():
    posts = Post.published.all()
    return Div(
        H2("Blog Posts"),
        *[Div(
            H3(A(post.title, href=f"/post/{post.slug}")),
            P(post.content),
            cls="post",
        ) for post in posts],
    )


layout = Main(
    Title("MyBlog"),
    Nav(
        A("MyBlog", href="/"),
        A("About", href="/about"),
        id="nav",
    ),
    H1("Welcome to MyBlog"),
    P("This is a simple blog built with Django and FastHTML."),
    post_list(),
    Footer(
        P("© 2021 MyBlog"),
    ),
    cls="container",
),

@app.get('/post/{slug}')
def post_detail(slug: str):
    post = Post.published.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    return Main(
        Title(post.title),
        Nav(
            A("MyBlog", href="/"),
            A("About", href="/about"),
            id="nav",
        ),
        H1(post.title),
        P(post.content),
        H3("Comments"),
        *[Div(
            H4(comment.name),
            P(comment.content),
            cls="comment",
        ) for comment in comments],
        Footer(
            P("© 2021 MyBlog"),
        ),
        cls="container",
    )

@app.get("/")
def home():
    return layout


serve()
