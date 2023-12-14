document.addEventListener("DOMContentLoaded", function() {
  // Get the login and registration forms
  const loginForm = document.getElementById("login-form");
  const registrationForm = document.getElementById("registration-form");

  // Check if the forms exist before accessing them
  if (loginForm) {
    // Get the submit button for the login form
    const loginSubmitButton = loginForm.querySelector('input[type="submit"]');
  
    // Function to check if all required inputs in a form have values
    function checkForm(form) {
      const requiredInputs = form.querySelectorAll('input[required]');
      for (const input of requiredInputs) {
        if (!input.value) {
          return false; // Return false if any required input is empty
        }
      }
      return true; // Return true if all required inputs have values
    }
  
    // Add event listener to the login form
    loginForm.addEventListener("input", function () {
      loginSubmitButton.disabled = !checkForm(loginForm);
    });
  }

  if (registrationForm) {
    // Get the submit button for the registration form
    const registrationSubmitButton = registrationForm.querySelector('input[type="submit"]');
    const emailField = registrationForm.querySelector('input[name="email_signup"]');
    const emailError = registrationForm.querySelector('#email-error');
    const submitButton = registrationForm.querySelector('#submit_register');

    // Function to check if all required inputs in a form have values
    function checkForm(form) {
      const requiredInputs = form.querySelectorAll('input[required]');
      for (const input of requiredInputs) {
        if (!input.value) {
          return false; // Return false if any required input is empty
        }
      }
      return true; // Return true if all required inputs have values
    }

    // Function to validate email
    function validateEmail(email) {
      const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
      return emailPattern.test(email);
    }

    // Add event listener to the registration form
    emailField.addEventListener("input", function () {
      registrationSubmitButton.disabled = !checkForm(registrationForm);

      // Validate email
      const emailValue = emailField.value.trim();
      if (validateEmail(emailValue)) {
        emailError.textContent = '';  // Clear the error message
        submitButton.disabled = false;  // Enable the submit button
      } else {
        emailError.textContent = 'Invalid email address';
        submitButton.disabled = true;  // Disable the submit button
      }
    });
  }

  const password_login = document.querySelector("#password_login");
  if(password_login != null){console.log("eye");}
  else{console.log("no-eye");}
  const eye = document.querySelector("#eye");
  eye.addEventListener("click", function(){
    console.log("eye");
    this.classList.toggle("fa-eye-slash");
    const type = password_login.getAttribute("type") === "password" ? "text" : "password";
    password_login.setAttribute("type", type);
  })
});