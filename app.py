from flask import Flask, render_template, request, redirect, url_for, flash
import time

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret"

SYSTEM_BUSY = True

@app.route('/')
def index():
    message = {
        'title': 'Jangan ragu untuk menghubungi kami.',
        'body': (
            'Sistem kami saat ini sedang mengalami penggunaan yang sangat tinggi, '
            'yang mungkin menyebabkan gangguan sementara pada proses verifikasi atau sinkronisasi kredensial. '
            'Silakan coba lagi setelah beberapa saat. Kami menghargai kesabaran dan pengertian Anda sementara kami berupaya menyelesaikan masalah ini.'
        )
    }
    return render_template('index.html', message=message, busy=SYSTEM_BUSY)

@app.route('/retry', methods=['POST'])
def retry():
    start = time.time()
    time.sleep(1.2)
    elapsed = time.time() - start

    if SYSTEM_BUSY:
        flash('Masih sibuk. Silakan coba lagi nanti.')
    else:
        flash('Verifikasi berhasil.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
