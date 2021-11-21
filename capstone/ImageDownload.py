import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyAL_GWBd8Pyg5x1Q3TBwTMpBk-rXo0IjaM",
    "authDomain": "characterrecognition47.firebaseapp.com",
    "projectId": "characterrecognition47",
    "storageBucket": "characterrecognition47.appspot.com",
    "messagingSenderId": "965124280348",
    "appId": "1:965124280348:web:a2705166d3c82d22fc8fd9",
    "measurementId": "G-BHSQ4LFS40",
    "databaseURL": ""
  }




def Image_Download():
    firebase = pyrebase.initialize_app(firebaseConfig)

    my_img = "uploads/image"
    local_img = "img.jpeg"
    storage = firebase.storage()
    storage.child(my_img).download(filename=local_img,path=".")