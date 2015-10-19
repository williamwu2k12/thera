from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    asset_paths = {"css_path": url_for('static', filename='index.css'),
            "city_image_path": url_for('static', filename='city.png'),
            "getstarted_image_path": url_for('static', filename='start.png'),
            "logo_image_path": url_for('static', filename="logo.png")
            }
    return render_template('index.html', **asset_paths) 

if __name__ == "__main__":
    app.debug = True
    app.run()
