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


class SEO(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    url_name = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(200), nullable=True)
    discription = db.Column(db.String(300), nullable=True)
    language = db.Column(db.String(20), nullable=False)
    note = db.Column(db.String(2000), nullable=True)
    
    def __repr__(self):
        return f'<seo {self.id}>'


class projects(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    short_discription = db.Column(db.String(2000), nullable=True)
    photo = db.Column(db.String(500), nullable=True)
    url = db.Column(db.String(100), nullable=True)
    url_name = db.Column(db.String(100), nullable=True)
    visibility = db.Column(db.String(50), default='visible', nullable=False)
    content = db.Column(db.String(50000), nullable=True)
    language = db.Column(db.String(20), nullable=False)
    priorities = db.Column(db.Integer)
    note = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<projects {self.id}>'  


class services(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    short_discription = db.Column(db.String(2000), nullable=True)
    photo = db.Column(db.String(500), nullable=True)
    url = db.Column(db.String(100), nullable=True)
    url_name = db.Column(db.String(100), nullable=True)
    visibility = db.Column(db.String(50), default='visible', nullable=False)
    content = db.Column(db.String(50000), nullable=True)
    language = db.Column(db.String(20), nullable=False)
    priorities = db.Column(db.Integer)
    note = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<services {self.id}>'


class Index(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True) 
    url = db.Column(db.String(100), nullable=True)
    url_name = db.Column(db.String(100), nullable=True)
    visibility = db.Column(db.String(50), default='visible', nullable=False)
    content = db.Column(db.String(50000), nullable=True)
    language = db.Column(db.String(20), nullable=False)
    note = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<index {self.id}>'


class contacts(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True) 
    url = db.Column(db.String(100), nullable=True)
    url_name = db.Column(db.String(100), nullable=True)
    visibility = db.Column(db.String(50), default='visible', nullable=False)
    content = db.Column(db.String(50000), nullable=True)
    language = db.Column(db.String(20), nullable=False)
    note = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<contacts {self.id}>'