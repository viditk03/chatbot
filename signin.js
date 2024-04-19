const firebaseConfig = {
    apiKey: "AIzaSyAb3tAr-BdrXo_A9US0Rf7LI2nAOqtjfzs",
    authDomain: "bandhu-4adbc.firebaseapp.com",
    databaseURL: "https://bandhu-4adbc-default-rtdb.firebaseio.com",
    projectId: "bandhu-4adbc",
    storageBucket: "bandhu-4adbc.appspot.com",
    messagingSenderId: "787273830286",
    appId: "1:787273830286:web:f098d2f5eb7f8fe5585edf",
    measurementId: "G-BLBC6MQJW9"
  }
  firebase.initializeApp(firebaseConfig);
  
  
  
  // Get a reference to the sign-up form
  const signinnForm = document.getElementById('signup-section');
  
  // Add an event listener to the form's 'submit' event
  signinnForm.addEventListener('submit', (event) => {
    // Prevent the form from submitting normally
    event.preventDefault();
  
    // Get the email and password inputs
    const emailInput = document.getElementById('email');
    const passInput = document.getElementById('pass');
  
    // Get the values of the email and password inputs
    const emailValue = emailInput.value;
    const passValue = passInput.value;
  
    // Authenticate the user with Firebase Authentication
    firebase.auth().createUserWithEmailAndPassword(emailValue, passValue)
      .then((userCredential) => {
        // User account created successfully
        const user = userCredential.user;
        console.log(`User account created for ${user.email}`);
  
        // Save the user data to Firebase Authentication
        return user.updateProfile({
          displayName: 'John Doe',
          photoURL: 'https://example.com/john-doe.jpg'
        });
      })
      .then(() => {
        // User data saved successfully
        console.log('User data saved to Firebase Authentication');
  
        // Show a pop-up alert
        alert('Sign-up successful! Welcome!');
      })
      .catch((error) => {
        // Error occurred during user account creation or user data save
        const errorCode = error.code;
        const errorMessage = error.message;
        console.error(`Error: ${errorCode} - ${errorMessage}`);
  
        // Show a pop-up alert with the error message
        alert(`Sign-up failed: ${errorMessage}`);
      });
  });
  // Handle clicks for the Google sign-in buttons
  // Define the googleSignIn function
  function googleSignIn() {
    const provider = new firebase.auth.GoogleAuthProvider();
  
    firebase.auth().signInWithPopup(provider)
      .then((userCredential) => {
        // User signed in successfully
        const user = userCredential.user;
  
        // Show a pop-up window
        alert('Sign-in successful!');
      })
      .catch((error) => {
        // Error occurred during sign-in
        const errorCode = error.code;
        const errorMessage = error.message;
  
        // Show a pop-up alert with the error message
        alert(`Sign-in failed: ${errorMessage}`);
      });
  }
  
  const button = document.getElementById('google-sign-in-button');
  button.addEventListener('click', googleSignIn);
  
  //login funnction
  const logInForm = document.getElementById('login-section');
  
  // Add an event listener to the form's 'submit' event
  logInForm.addEventListener('submit', (event) => {
    // Prevent the form from submitting normally
    event.preventDefault();
  
    // Get the email and password inputs
    const emailInput = logInForm.querySelector('input[type="email"]');
    const passInput = logInForm.querySelector('input[type="password"]');
  
    // Get the values of the email and password inputs
    const emailValue = emailInput.value;
    const passValue = passInput.value;
  
    // Authenticate the user with Firebase Authentication using email and password
    firebase.auth().signInWithEmailAndPassword(emailValue, passValue)
      .then((userCredential) => {
        // User signed in successfully
        const user = userCredential.user;
        console.log(`User signed in for ${user.email}`);
  
        // Show a pop-up alert
        alert('Sign-in successful!');
  
        // Redirect to a blank page
        window.location.href = '/chatbot/chatbox.html';
      })
      .catch((error) => {
        // Error occurred during sign-in
        const errorCode = error.code;
        const errorMessage = error.message;
        console.error(`Error: ${errorCode} - ${errorMessage}`);
  
        // Show a pop-up alert with the error message
        alert(`log-in failed: ${errorMessage}`);
      });
  });
  
  //iconn loginn
  const auth = firebase.auth();
  
  // Set up Google sign-in provider
  const provider = new firebase.auth.GoogleAuthProvider();
  
  // Get the sign-in button element
  const signInButton = document.getElementById('google-log-in');
  
  // Add click event listener to the sign-in button
  signInButton.addEventListener('click', () => {
    // Sign in with Google
    auth.signInWithPopup(provider)
      .then((result) => {
        // User signed in successfully
        const user = result.user;
  
        // Display pop-up message
        alert(`Signed in as ${user.displayName}`);
  
        // Redirect to blank page
        window.location.href = '/chatbot/chatbox.html';
      })
      .catch((error) => {
        // Display error message
        alert(`Sign-in failed: ${error.message}`);
      });
  });
  
  function scrollToElement(elementSelector, instance = 0) {
    // Select all elements that match the given selector
    const elements = document.querySelectorAll(elementSelector);
    // Check if there are elements matching the selector and if the requested instance exists
    if (elements.length > instance) {
      // Scroll to the specified instance of the element
      elements[instance].scrollIntoView({ behavior: 'smooth' });
    }
  }
  
