import sys
import os
sys.path.insert(1,os.path.join(os.path.abspath('.'),'venv/lib/python2.7/site-packages'))
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


if __name__ == '__main__':
    app.run(debug=True)

