from app import app


@app.route('/')
def index():
    return "<style>html{background-color:#FFOOFF} p{font-size:15px}</style><p><a href='https://www.google.com' style = 'color:#00FF00'>Badimpadump</a></p>"


@app.route("/<int:page_num>")
def easter_egg(page_num):
    return f"<p style='font-size:75px;'>The square of {page_num} is <b>{page_num**2}</b></p>"
