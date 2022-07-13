// These are all querySelectors used to grab the fields to read and post there value to the server,
// as well as some fields which will display success or error messages depending on the post back from the server

const emailField = document.querySelector("#yourEmail");
const emailFeedBackArea = document.querySelector(".invalid-feedback");
const emailSuccessOutput = document.querySelector(".emailSuccessOutput");

const submitBtn = document.querySelector("#user-auth-sumbit-btn");

// Verify Email Ajax Validation
emailField.addEventListener("focusout", (e) => {
  const emailVal = e.target.value;

  emailSuccessOutput.style.display = "block";

  emailSuccessOutput.innerHTML = '<i class="bi bi-arrow-repeat"></i>  '+`Checking  ${emailVal}`;

  emailField.classList.remove("is-valid");
  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/Auth/validate-login/", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        emailSuccessOutput.style.display = "none";
        console.log("data", data);
        if (data.email_error) {
          submitBtn.disabled = true;
          emailField.classList.add("is-invalid");
          emailFeedBackArea.style.display = "block";
          // submitBtn.classList.add("btn--dark-lighter");
          emailFeedBackArea.innerHTML = `<p class="text-danger">${data.email_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
          emailField.classList.add("is-valid");
          // submitBtn.classList.remove("btn--dark-lighter");
        }
      });
  }
});
