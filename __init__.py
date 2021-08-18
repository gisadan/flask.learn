

from flaskext.markdown import Markdown



def create_app():

# --------------------------------- [edit] ---------------------------------- #
    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])
# --------------------------------------------------------------------------- #

    return app