from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""
    if request.method == "POST":
        ekspresi = request.form.get("ekspresi")
        try:
            hasil = eval(ekspresi)   # ⚠️ hanya untuk demo, hati-hati eval!
        except:
            hasil = "Error"
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
