import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load
app = Flask(__name__)
model = load('final.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[int(x) for x in request.form.values()]]
    print(x_test)
    if(x_test[0][5] == 0):
        x_test[0][0]=0
        x_test[0].insert(0,0)
        x_test[0].insert(1,0)
    elif(x_test[0][5] == 1):
        x_test[0][0]=0
        x_test[0].insert(1,0)
        x_test[0].insert(1,1)
    elif(x_test[0][5] == 2):
        x_test[0][0]=0
        x_test[0].insert(0,0)
        x_test[0].insert(1,1)
    elif(x_test[0][5] == 3):
        x_test[0][0]=0
        x_test[0].insert(0,1)
        x_test[0].insert(1,1)
    else:
        x_test[0][0]=0
        x_test[0].insert(1,1)
        x_test[0].insert(0,0)
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    return render_template('index.html', prediction_text='Profit {}'.format(output))

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.y_predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
