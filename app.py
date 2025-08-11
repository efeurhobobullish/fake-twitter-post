from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    tweet = None
    if request.method == 'POST':
        profile_pic = request.files.get('profile_pic')
        verified = request.form.get('verified') == 'on'

        if profile_pic:
            filename = secure_filename(profile_pic.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            profile_pic.save(filepath)
            profile_pic_url = url_for('static', filename=f'uploads/{filename}')
        else:
            profile_pic_url = ''

        tweet = {
            'name': request.form.get('name'),
            'handle': request.form.get('handle'),
            'profile_pic': profile_pic_url,
            'content': request.form.get('content'),
            'date': request.form.get('date'),
            'likes': request.form.get('likes'),
            'retweets': request.form.get('retweets'),
            'verified': verified,
        }
    return render_template('index.html', tweet=tweet)

if __name__ == '__main__':
    app.run(debug=True)
