import pyrebase

config = {
  'apiKey': "AIzaSyBLCdqXHMYP-Hm0maNclOpiWK-UsiQ-Eto",
  'authDomain' : "medify-37830.firebaseapp.com",
  'databaseURL': "https://medify-37830-default-rtdb.firebaseio.com",
  'projectId' : "medify-37830",
  'storageBucket' : "medify-37830.appspot.com",
  'messagingSenderId' : "882712357939",
  'appId' : "1:882712357939:web:f924a4b3f753079639c746",
  'measurementId' : "G-5H0GB0Z7WQ"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()
auth = firebase.auth()

"""
Structure for Medical Info
{ "name" : ~~~ 
  "age" : ~~~
  "weight" : ~~~
  "height" : ~~~
  "blood type" : ~~~
  "dlid" : ~~~
  "medical conditions" : [~~~]
  "allergies" : [~~~]
  "medication" : [~~~]}
"""


def login(email, password):
    return auth.sign_in_with_email_and_password(email, password)


def create_acct(email, password):
    auth.create_user_with_email_and_password(email, password)


def verify_emt(ems_id):
    emt_list = database.child("emts").get().val()
    return ems_id in emt_list


def update_patient_info(info):
    patients = database.child("patients").get().val()
    if info["dlid"] in patients:
        for key in info:
            database.child("patients").child(info["dlid"]).update({key: info[key]})
    else:
        database.child("patients").push({info["dlid"] : info})


def get_patient_info(dlid):
    patient_info = database.child("patients").child(dlid).get().val()
    return patient_info


# Unit Test #1: User Login --> Passed
user = login("bun@njit.edu", "abcdefg")
print(verify_emt("101010"))
print(user["idToken"])

# Unit Test #2: Create Acct --> Passed
# create_acct("jt123@njit.edu", "abcdefgh")

# Unit Test #3: Verify EMS
print(verify_emt("10100"))

# Unit Test #4: Update Patient Info
info = {  "name" : "Jonas",
          "age" : "15",
          "weight" : "145",
          "height" : "5'10",
          "blood type" : "B",
          "dlid" : "1232441",
          "medical conditions" : "Autism",
          "allergies" : "Sound",
          "medication" : "Crack"
}
update_patient_info(info)

# Unit Test #5: Get Patient Info
print(get_patient_info("12312441"))

