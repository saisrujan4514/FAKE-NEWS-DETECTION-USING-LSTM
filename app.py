from flask import Flask, redirect,render_template,request, url_for,jsonify
from tensorflow.keras.preprocessing.text import Tokenizer #tokenize the text data
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import model_from_json
from keras_preprocessing.text import tokenizer_from_json
from json import load
app=Flask(__name__,template_folder='tempalete')
def create_model():    
    with open("model.json","r") as file:
        model_json=file.read()
    loaded_model=model_from_json(model_json)
    #print(loaded_model.summary())
    loaded_model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])
    loaded_model.load_weights("weights.h5")
    return loaded_model
model=create_model()
with open('tokenizer.json') as f:
            data = load(f)
            tokenizer = tokenizer_from_json(data)

@app.route('/')
def home():
    return render_template('index1.html',s1="huhu")

@app.route('/newscheck')
def newscheck():
    textname = request.args.get('news')
    maxlen=1000
    x=[textname]
    print(x)
    x=tokenizer.texts_to_sequences(x)
    x=pad_sequences(x,maxlen=maxlen)
    pred=(model.predict(x)>=0.5).astype(int).any()
    if (model.predict(x)>=0.5).astype(int).any()==True:
                    print("True")
                    return jsonify(result ="REAL")
    else:
                    print("False")
                    return jsonify(result ="FAKE")
@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us_email():
    """name1 = request.form['name1']
    email1 = request.form['email1']
    phoneno1 = request.form['phoneno1']
    feedback1 = request.form['feedback1']
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("project324514@gmail.com","Project324514@")
    server.sendmail("project324514@gmail.com",email1,feedback1)"""
    """msg = Message("
                'Hello',
                sender ='project324514@gmail.com',
                recipients = ['mohan.saisrujan4@gmail.com']
               )
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)"""
    return render_template('index1.html')

if __name__=="__main__":
    app.run(port=56482,debug=True)