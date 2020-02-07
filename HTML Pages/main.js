  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyDcSAovQgYc5QrVPys2OqUp6t967ic7pHI",
    authDomain: "oasis-initiative.firebaseapp.com",
    databaseURL: "https://oasis-initiative.firebaseio.com",
    projectId: "oasis-initiative",
    storageBucket: "oasis-initiative.appspot.com",
    messagingSenderId: "1085620518416",
    appId: "1:1085620518416:web:0bb68af6dc940f7e4f1495",
    measurementId: "G-15N5RJ54ZZ"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();


  // Reference messages collection
var messagesRef = firebase.database().ref('contactformmessages');
var storage = firebase.storage();


$('#uploadForm').submit(function(e) {
    e.preventDefault();
 
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
        name: $('.fullname').val(),
        email: $('.email').val(),
        subject: $('.subject').val(),
        message: $('.message').val()
    });

    $('.success-message').show();

    $('#uploadForm')[0].reset();
});