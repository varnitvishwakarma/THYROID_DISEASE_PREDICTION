from flask import Flask,render_template,request,app
import pickle
from flask import Response


tree_model = pickle.load(open("E:/ML PROJECTS/THYROID DISEASE PREDICTION/artifacts/model.pkl", "rb"))




application = Flask(__name__)
app=application




@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/predict",methods=["GET","POST"])
def predict_data():
     if request.method == "POST":
        AGE = int(request.form.get("Age"))
        GENDER = request.form.get("Gender")
        if  GENDER== "Male":
            GENDER = 1
        else:
            GENDER = 0

        Free_T4 = request.form.get("Free_T4")
        if Free_T4 == "True":
            Free_T4 = 1
        else:
            Free_T4 = 0

        TSH = request.form.get("TSH")
        if TSH == "True":
            TSH = 1
        else:
            TSH = 0

        T3 = request.form.get("T3")
        if T3 == "True":
            T3 = 1
        else:
            T3 = 0

        TT4 = request.form.get("TT4")
        if TT4 == "True":
            TT4 = 1
        else:
            TT4 = 0

        FTI = request.form.get("FTI")
        if FTI == "True":
            FTI = 1
        else:
            FTI = 0

        TBG = request.form.get("TBG")
        if TBG == "True":
            TBG = 1
        else:
            TBG = 0

        Pregnant = request.form.get("Pregnant")
        if Pregnant == "True":
            Pregnant = 1
        else:
            Pregnant = 0

        Goitre = request.form.get("Goitre")
        if Goitre == "True":
            Goitre = 1
        else:
            Goitre = 0

        result = ""
        new_data = [[AGE,GENDER,Free_T4, TSH, T3, TT4, FTI, TBG, Pregnant, Goitre]]

        results = tree_model.predict(new_data)
        if results == 0:
            results = "According to the analysis, you do not have thyroid"
        else:
            results = "According to the analysis, you have thyroid"

        return render_template("predict.html",result=results)

     else:
        return render_template("predict.html")
   
   
   

if __name__=="__main__":
    app.run(host="0.0.0.0")