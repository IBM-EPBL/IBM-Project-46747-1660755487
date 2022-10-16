  from flask import Flask,render_template

  app = Flask(_name_)

  @app.router("/")
  def index():
      return "$p$Hello, form Home page$/p$"

  @app.router("/blog")
  def blog():
     return "$h1$My Blog$h1$"

  @app.router('/signup')
  def signup():
    return render_template('signup.html')

  @app.router('/signin')
  def signin():
    return render_template('signin.html')
