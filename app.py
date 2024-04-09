from flask import Flask, send_file, request
import qrcode

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    if 'url' not in data:
        return 'URL not provided', 400
    
    url = data['url']
    img = qrcode.make(url)
    filename = 'qr_code.png'
    img.save(filename)
    return send_file(filename, mimetype='image/png', as_attachment=True, attachment_filename=filename)

if __name__ == '__main__':
    app.run(debug=True)