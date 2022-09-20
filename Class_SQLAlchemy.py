from extensions import db


class Menu(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=True)
    url_name = db.Column(db.String(100), nullable=True)
    visibility = db.Column(db.String(50), default='visible', nullable=False)
    button_type = db.Column(db.String(50), nullable=False)
    parent = db.Column(db.String(50))
    language = db.Column(db.String(20), nullable=False)
    priorities = db.Column(db.Integer)
    note = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<menu {self.id}>'  


# class index(db.Model):
# class services(db.Model):
# class projects(db.Model):
# class contacts(db.Model):

# class Projects(db.Model):
# class Services(db.Model):

# class SEO(db.Model):