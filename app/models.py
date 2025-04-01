from datetime import date
from app import db
from sqlalchemy.ext.hybrid import hybrid_property


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", backref=db.backref("books", lazy=True))
    genre = db.Column(db.String(200), index=True)
    publish_date = db.Column(db.Date, index=True)

    def __str__(self):
        return f"<Book '{self.title}'>"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    surname = db.Column(db.String(100), index=True)

    __table_args__ = (
        db.UniqueConstraint('name', 'surname', name='_name_surname_uc'),
    )

    def full_name(self):
        return f"{self.name} {self.surname}>"

    def __str__(self):
        return f"Author '{self.full_name()}'"


class CheckoutRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    book = db.relationship('Book', backref=db.backref('checkout_records', lazy=True))
    borrow_date = db.Column(db.Date, index=True)
    return_date = db.Column(db.Date, index=True)
    _is_borrowed = db.Column(db.Boolean, unique=False, default=False)

    @hybrid_property
    def is_borrowed(self):
        if self.borrow_date and self.return_date:
            return self.borrow_date <= date.today() <= self.return_date
        return False

    @is_borrowed.setter
    def is_borrowed(self, value):
        self._is_borrowed = value

    def __str__(self):
        return f"<Checkout Record for {self.book.title}. \nIs book checked out: {self.is_borrowed}>"