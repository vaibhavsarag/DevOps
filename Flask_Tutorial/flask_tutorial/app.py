from flask import Flask, request, render_template
from datetime import datetime
import pymongo

from dotenv import load_dotenv
import os


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)


database = client.test

collection = database['flask_tutorial']

 

# Create a new client and connect to the server


# Send a ping to confirm a successful connection
#try:
 #   client.admin.command('ping')
  #  print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
 #   print(e)

app = Flask(__name__)

@app.route('/')

def home():
    dayofweek = datetime.now().strftime("%A")
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', day=dayofweek, time=current_time)  

@app.route('/submit', methods=['POST'])
def submit():
    from_data = dict(request.form)
    collection.insert_one(from_data)
    return from_data

    
if __name__ == '__main__':
    app.run(debug=True)