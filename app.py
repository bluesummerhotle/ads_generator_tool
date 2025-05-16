from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        product_name = request.form['product_name']
        keywords = request.form['keywords']
        usp = request.form['usp']
        location = request.form['location']
        cta = request.form['cta']

        results = [
            {
                'Headline 1': f"{product_name} Thiết Kế Riêng",
                'Headline 2': f"{usp[:30]}",
                'Headline 3': f"{cta[:30]}",
                'Description 1': f"{product_name} tại {location}. {usp}.",
                'Description 2': f"{cta}. Liên hệ ngay!"
            },
            {
                'Headline 1': f"{keywords.split(',')[0].strip().capitalize()} Giá Tốt",
                'Headline 2': f"Giao hàng {location}",
                'Headline 3': f"{cta[:30]}",
                'Description 1': f"Tìm hiểu về {product_name} với {usp}.",
                'Description 2': f"{cta}. Miễn phí tư vấn."
            }
        ]

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
