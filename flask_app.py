import numpy as np
import pickle
from flask import Flask, request, render_template
app = Flask(__name__)

loaded_model = pickle.load(open(xg20, 'rb'))

def pp_Gender(Gender):
    Gender = 0

    if Gender == 'Female':
        Gender = 1
    elif Gender == 'Male':
        Gender = 0

    return Gender

def pp_CreditTerm(AMT_ANNUITY, AMT_CREDIT):
    
    CreditTerm = AMT_ANNUITY / AMT_CREDIT
    
    return CreditTerm

def pp_CGDiff(AMT_CREDIT, AMT_GOODS_PRICE):
    
    CGDiff = AMT_CREDIT - AMT_GOODS_PRICE

    return CGDiff

def pp_EduType(EduType):
    EduType=0
   
    if  EduType =='spesial':
        EduType = 135000
    elif  EduType =='Higher':
        EduType = 180000
    elif EduType =='IncompleteHigher':
        EduType = 157500
    elif EduType =='LowerSecondary':
        EduType = 112500
    elif EduType =='Academicdegree':
        EduType = 211500

    return EduType

def pp_CAP(AMT_CREDIT, AMT_ANNUITY ):
    
    CAP = AMT_CREDIT / AMT_ANNUITY
    
    return CAP

def pp_ALF(DAYS_BIRTH, AMT_CREDIT, AMT_ANNUITY ):
    
    ALF = DAYS_BIRTH *(-1.0/365) + AMT_CREDIT / AMT_ANNUITY
    
    return ALF

def pp_CABP(OWN_CAR_AGE, DAYS_BIRTH):
    
    CABP = OWN_CAR_AGE / DAYS_BIRTH
    
    return CABP

def pp_CAEP(OWN_CAR_AGE, DAYS_EMPLOYED):
    
    CAEP = OWN_CAR_AGE / DAYS_EMPLOYED
    
    return CAEP

def pp_AIP(AMT_ANNUITY, AMT_INCOME_TOTAL):
    
    AIP = AMT_ANNUITY / AMT_INCOME_TOTAL
    
    return AIP

def pp_ALEP(CREDIT_TERM, DAYS_EMPLOYED):
    
    ALEP = CREDIT_TERM / DAYS_EMPLOYED
    
    return ALEP

def pp_BEP(DAYS_EMPLOYED, DAYS_BIRTH):
    
    BEP = DAYS_EMPLOYED / DAYS_BIRTH
    
    return BEP

def pp_CIP(AMT_ANNUITY, AMT_INCOME_TOTAL):
    
    CIP = AMT_ANNUITY / AMT_INCOME_TOTAL
    
    return CIP

def pp_days(age):
    
    daysbirth = age * -365
    
    return daysbirth


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    prediction_text = ''

    if request.method == 'POST':
        EXT_SOURCE_1 = float(request.form["EXT_SOURCE_1"])
        EXT_SOURCE_2 = float(request.form["EXT_SOURCE_2"])
        EXT_SOURCE_3 = float(request.form["EXT_SOURCE_3"])
        AMT_CREDIT = float(request.form["AMT_CREDIT"])
        DAYS_ID_PUBLISH = pp_days(float(request.form["DAYS_ID_PUBLISH"]))
        DAYS_BIRTH = pp_days(float(request.form["DAYS_BIRTH"]))
        AMT_GOODS_PRICE =float(request.form["AMT_GOODS_PRICE"])
        AMT_ANNUITY = float(request.form["AMT_ANNUITY"])
        DAYS_EMPLOYED = pp_days(float(request.form["DAYS_EMPLOYED"]))
        
        CREDIT_TERM = pp_CreditTerm(float(request.form["AMT_ANNUITY"]),float(request.form["AMT_CREDIT"]))
        CREDIT_GOODS_DIFF = pp_CGDiff(float(request.form["AMT_CREDIT"]),float(request.form["AMT_GOODS_PRICE"]))
        CREDIT_ANNUITY_PERCENT =pp_CAP(float(request.form["AMT_CREDIT"]),float(request.form["AMT_ANNUITY"]))
        AGE_LOAN_FINISH =pp_ALF(DAYS_BIRTH,float(request.form["AMT_CREDIT"]), float(request.form["AMT_ANNUITY"]))
        CAR_AGE_EMP_PERCENT = pp_CAEP(float(request.form["OWN_CAR_AGE"]),DAYS_EMPLOYED)
        MEDIAN_INCOME_EDU_TYPE = pp_EduType(str(request.form["EDUCATION_TYPE"]))
        CAR_AGE_BIRTH_PERCENT = pp_CABP(float(request.form["OWN_CAR_AGE"]),DAYS_BIRTH)
        CODE_GENDER_F = pp_Gender(str(request.form["Sex"]))
        ANNUITY_INCOME_PERCENT = pp_AIP(float(request.form["AMT_ANNUITY"]),float(request.form["AMT_INCOME_TOTAL"]))
        ANNUITY_LENGTH_EMPLOYED_PERCENT = pp_ALEP(CREDIT_TERM,DAYS_EMPLOYED)
        BIRTH_EMPLOYED_PERCENT = pp_BEP(DAYS_EMPLOYED,DAYS_BIRTH)
        CREDIT_INCOME_PERCENT = pp_CIP(float(request.form["AMT_CREDIT"]),float(request.form["AMT_INCOME_TOTAL"]))
                 
        final_features = [EXT_SOURCE_1,EXT_SOURCE_2,EXT_SOURCE_3,AMT_CREDIT,DAYS_ID_PUBLISH,DAYS_BIRTH,AMT_GOODS_PRICE, AMT_ANNUITY, CREDIT_TERM,CREDIT_GOODS_DIFF, CREDIT_ANNUITY_PERCENT, AGE_LOAN_FINISH, CAR_AGE_EMP_PERCENT, MEDIAN_INCOME_EDU_TYPE, CAR_AGE_BIRTH_PERCENT, CODE_GENDER_F, ANNUITY_INCOME_PERCENT, ANNUITY_LENGTH_EMPLOYED_PERCENT, BIRTH_EMPLOYED_PERCENT, CREDIT_INCOME_PERCENT]

        prediction = loaded_model.predict([final_features])

        output = prediction[0]

        if output == 1:
            prediction_text = 'SORRY'
        elif output == 0:
            prediction_text = 'DEAL'

    return render_template('index.html', prediction_text=prediction_text )

if __name__ == "__main__":
    app.run(debug=True)
