from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(300), nullable=False)
    name = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'Book {self.id}: {self.author} - {self.name}'


@app.route('/')
def main():
    books = Book.query.all()
    return render_template('task.html', books=books)


@app.route('/add', methods=['POST'])
def add_book():
    data = request.json
    author = data.get('author')
    name = data.get('name')

    if not author or not name:
        return jsonify({'success': False, 'message': 'Author and name are required'}), 400


    new_book = Book(author=author, name=name)
    db.session.add(new_book)
    db.session.commit()


    return jsonify({
        'success': True,
        'book': {
            'id': new_book.id,
            'author': new_book.author,
            'name': new_book.name,
        }
    })

@app.route('/clear', methods=['POST'])
def clear_books():
    try:
        db.session.query(Book).delete()
        db.session.commit()
        return jsonify({'success': True, 'message': 'All books cleared'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)