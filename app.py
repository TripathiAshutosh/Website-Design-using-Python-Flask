from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route('/demo-models',methods=["Get","POST"])
def demoModels():
    return render_template("demo-models.html")


@app.route('/getResponseLinearReg',methods=["GET","POST"])
def getResponseLinearReg():
    print("inside python")
    CRIM = request.form["CRIM"]
    ZN = request.form["ZN"]
    INDUS = request.form["INDUS"]
    CHAS = request.form["CHAS"]
    NOX = request.form["NOX"]
    RM = request.form["RM"]
    AGE = request.form["AGE"]
    DIS = request.form["DIS"]
    RAD = request.form["RAD"]
    TAX = request.form["TAX"]
    PT = request.form["PT"]
    B = request.form["B"]
    LSTAT = request.form["LSTAT"]
    inputList = [CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PT,B,LSTAT]
    with open("/boston_mlm.pkl", 'rb') as file:
            pickle_model = pickle.load(file)
            y_pred_from_pkl = pickle_model.predict([inputList])
    print(y_pred_from_pkl)
    return str(y_pred_from_pkl[0])



@app.route('/contact',methods=["Get","POST"])
def contact():
    return render_template("contact.html")
    
if __name__ == '__main__':
    app.run(debug=True)
