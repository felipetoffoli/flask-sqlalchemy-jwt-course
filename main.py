from app import create_app, db
from flask_migrate import Migrate
from app.src.models import User
from app.src.models import Contact



app = create_app("develoment")

Migrate(app, db)


@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Contact=Contact
    )
app.run(debug=True)
