document.addEventListener("DOMContentLoaded", function() {
  const loginForm = document.getElementById("login-form");
  const registrationForm = document.getElementById("registration-form");

  if (loginForm) {
    const loginSubmitButton = loginForm.querySelector('input[type="submit"]');
  
    function checkForm(form) {
      const requiredInputs = form.querySelectorAll('input[required]');
      for (const input of requiredInputs) {
        if (!input.value) {
          return false; 
        }
      }
      return true; 
    }
  
    loginForm.addEventListener("input", function () {
      loginSubmitButton.disabled = !checkForm(loginForm);
    });
  }

  if (registrationForm) {
    const registrationSubmitButton = registrationForm.querySelector('input[type="submit"]');
    const emailField = registrationForm.querySelector('input[name="email_signup"]');
    const emailError = registrationForm.querySelector('#email-error');
    const submitButton = registrationForm.querySelector('#submit_register');

    function checkForm(form) {
      const requiredInputs = form.querySelectorAll('input[required]');
      for (const input of requiredInputs) {
        if (!input.value) {
          return false; 
        }
      }
      return true; 
    }

    function validateEmail(email) {
      const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
      return emailPattern.test(email);
    }

    emailField.addEventListener("input", function () {
      registrationSubmitButton.disabled = !checkForm(registrationForm);

      const emailValue = emailField.value.trim();
      if (validateEmail(emailValue)) {
        emailError.textContent = '';  
        submitButton.disabled = false;  
      } else {
        emailError.textContent = 'Invalid email address';
        submitButton.disabled = true; 
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