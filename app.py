from flask import Flask, render_template, request
import pandas as pd
import os

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

        # Tạo tiêu đề và mô tả cơ bản (hardcode mẫu cho bước 1)
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

@app.route('/download', methods=['POST'])
def download():
    data = request.form.get('data')
    df = pd.read_json(data)
    df.to_csv('ads_output.csv', index=False)
    return "<h3>Đã xuất ra file ads_output.csv thành công!</h3>"

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')
    app.run(debug=True, port=5000)
