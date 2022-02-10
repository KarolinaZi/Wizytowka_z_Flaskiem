from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def me():
    return render_template("wizytowka_child_me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
       print("We received GET")
       return render_template("wizytowka_child_kontakt.html")
    elif request.method == 'POST':
        print("We received POST")
        d = request.form
        print(d.get('textarea'))
        #return redirect("/mypage/contact")
        return "Message sent"


#if __name__ == '__main__':
#    app.run(debug=True)