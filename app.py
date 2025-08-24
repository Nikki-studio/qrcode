from flask import  Flask, render_template,request
import qrcode_utils
import io ,os,json
from qrcode_utils import iterate_links

if not os.path.exists("paths.json"):
    with open("paths.json","w") as f:
        json.dump({"count":0,"paths":[]},f)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    link = request.form.get('url')
    file = request.files.get('file')
    list_of_links = []
    if link:
        list_of_links.append(link)
    if file and file.filename!='':
        stream = io.StringIO(file.stream.read().decode("utf-8"))
        for line in stream.readlines():
            list_of_links.append(line.strip())
    return render_template('index.html', paths=iterate_links(list_of_links))

