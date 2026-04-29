from flask import Flask, render_template

app = Flask(__name__)

# Sample data for perfumes
perfumes = [
    {"name": "Midnight Oud", "type": "Men", "img": "https://images.unsplash.com/photo-1523293182086-7651a899d37f?q=80&w=600", "price": "$85"},
    {"name": "Rose Elixir", "type": "Women", "img": "https://images.unsplash.com/photo-1541643600914-78b084683601?q=80&w=600", "price": "$95"},
    {"name": "Velvet Sandalwood", "type": "Unisex", "img": "https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=600", "price": "$110"},
    {"name": "Oceanic Blue", "type": "Men", "img": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?q=80&w=600", "price": "$75"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/collection/<category>')
def collection(category):
    filtered = [p for p in perfumes if p['type'].lower() == category.lower()]
    return render_template('collection.html', perfumes=filtered, category=category)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)