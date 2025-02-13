from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")

        # نمایش اطلاعات در کنسول
        print(f"نام: {name}, شماره تلفن: {phone}")

        return f"اطلاعات دریافت شد! <br> نام: {name} <br> شماره تلفن: {phone}"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)