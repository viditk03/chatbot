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
var overlay = document.getElementById("overlay");

// Buttons to 'switch' the page
var openSignUpButton = document.getElementById("slide-left-button");
var openSignInButton = document.getElementById("slide-right-button");

// The sidebars
var leftText = document.getElementById("sign-in");
var rightText = document.getElementById("sign-up");

// The forms
var accountForm = document.getElementById("sign-in-info")
var signinForm = document.getElementById("sign-up-info");

// Open the Sign Up page
openSignUp = () =>{
  // Remove classes so that animations can restart on the next 'switch'
  leftText.classList.remove("overlay-text-left-animation-out");
  overlay.classList.remove("open-sign-in");
  rightText.classList.remove("overlay-text-right-animation");
  // Add classes for animations
  accountForm.className += " form-left-slide-out"
  rightText.className += " overlay-text-right-animation-out";
  overlay.className += " open-sign-up";
  leftText.className += " overlay-text-left-animation";
  // hide the sign up form once it is out of view
  setTimeout(function(){
    accountForm.classList.remove("form-left-slide-in");
    accountForm.style.display = "none";
    accountForm.classList.remove("form-left-slide-out");
  }, 700);
  // display the sign in form once the overlay begins moving right
  setTimeout(function(){
    signinForm.style.display = "flex";
    signinForm.classList += " form-right-slide-in";
  }, 200);
}

// Open the Sign In page
openSignIn = () =>{
  // Remove classes so that animations can restart on the next 'switch'
  leftText.classList.remove("overlay-text-left-animation");
  overlay.classList.remove("open-sign-up");
  rightText.classList.remove("overlay-text-right-animation-out");
  // Add classes for animations
  signinForm.classList += " form-right-slide-out";
  leftText.className += " overlay-text-left-animation-out";
  overlay.className += " open-sign-in";
  rightText.className += " overlay-text-right-animation";
  // hide the sign in form once it is out of view
  setTimeout(function(){
    signinForm.classList.remove("form-right-slide-in")
    signinForm.style.display = "none";
    signinForm.classList.remove("form-right-slide-out")
  },700);
  // display the sign up form once the overlay begins moving left
  setTimeout(function(){
    accountForm.style.display = "flex";
    accountForm.classList += " form-left-slide-in";
  },200);
}

// When a 'switch' button is pressed, switch page
openSignUpButton.addEventListener("click", openSignUp, false);
openSignInButton.addEventListener("click", openSignIn, false);

// Get a reference to the sign-up form
const signUpForm = document.getElementById('sign-up-form');

// Add an event listener to the form's 'submit' event
signUpForm.addEventListener('submit', (event) => {
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
// icnon onclick signup
function handleIconClick() {
  // Authenticate the user with Firebase Google Authentication API
  const provider = new firebase.auth.GoogleAuthProvider();
  firebase.auth().signInWithPopup(provider)
    .then((result) => {
      // User account created successfully
      const user = result.user;
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
    })
    .catch((error) => {
      // Error occurred during user account creation or user data save
      const errorCode = error.code;
      const errorMessage = error.message;
      console.error(`Error: ${errorCode} - ${errorMessage}`);
    });
}
//login funnction
const signInForm = document.getElementById('sign-in-form');

// Add an event listener to the form's 'submit' event
signInForm.addEventListener('submit', (event) => {
  // Prevent the form from submitting normally
  event.preventDefault();

  // Get the email and password inputs
  const emailInput = signInForm.querySelector('input[type="email"]');
  const passInput = signInForm.querySelector('input[type="password"]');

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
      window.location.href = 'about:blank';
    })
    .catch((error) => {
      // Error occurred during sign-in
      const errorCode = error.code;
      const errorMessage = error.message;
      console.error(`Error: ${errorCode} - ${errorMessage}`);

      // Show a pop-up alert with the error message
      alert(`Sign-in failed: ${errorMessage}`);
    });
});
//iconn signup
const googleSignInIcons = document.querySelectorAll('.icon');

// Add a click event listener to each Google sign-in icon
googleSignInIcons.forEach((icon) => {
  icon.addEventListener('click', () => {
    // Authenticate the user with Firebase Authentication using Google sign-in
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(provider)
      .then((userCredential) => {
        // User signed in successfully
        const user = userCredential.user;
        console.log(`User signed in for ${user.email}`);

        // Show a pop-up alert
        alert('Sign-in successful!');

        // Redirect to a blank page using window.location.replace and cache-busting
        window.location.replace('about:blank?v=' + new Date().getTime());
      })
      .catch((error) => {
        // Error occurred during sign-in
        const errorCode = error.code;
        const errorMessage = error.message;
        console.error(`Error: ${errorCode} - ${errorMessage}`);

        // Show a pop-up alert with the error message
        alert(`Sign-in failed: ${errorMessage}`);
      });
  });
});