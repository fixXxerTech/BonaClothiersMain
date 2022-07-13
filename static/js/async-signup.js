// These are all querySelectors used to grab the fields to read and post there value to the server,
// as well as some fields which will display success or error messages depending on the post back from the server

const usernameField = document.querySelector("#yourUsername");
const feedBackArea = document.querySelector(".usernameFeedBackArea");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");

// const phoneField = document.querySelector("#userphone");
// const phoneFeedBackArea = document.querySelector(".phoneFeedBackArea");
// const phoneSuccessOutput = document.querySelector(".phoneSuccessOutput");

const emailField = document.querySelector("#yourEmail");
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const emailSuccessOutput = document.querySelector(".emailSuccessOutput");

const submitBtn = document.querySelector("#user-auth-sumbit-btn");


// Verify Phone Ajax Validation
// phoneField.addEventListener("input", (e) => {
//   const userphoneVal = e.target.value;

//   phoneSuccessOutput.style.display = "block";

//   phoneSuccessOutput.innerHTML = '<i class="bi bi-arrow-repeat"></i>  '+`Checking  ${userphoneVal}`;

//   phoneField.classList.remove("is-valid");
//   phoneField.classList.remove("is-invalid");
//   phoneFeedBackArea.style.display = "none";

//   if (userphoneVal.length > 0) {
//     fetch("/Auth/validate-phonenumber/", {
//       body: JSON.stringify({ userphonenumber: userphoneVal }),
//       method: "POST",
//     })
//       .then((res) => res.json())
//       .then((data) => {
//         phoneSuccessOutput.style.display = "none";
//         console.log("data", data);
//         if (data.userphone_error) {
//           submitBtn.disabled = true;
//           phoneField.classList.add("is-invalid");
//           phoneFeedBackArea.style.display = "block";
//           phoneFeedBackArea.innerHTML = `<p class="text-danger">${data.userphone_error}</p>`;
//           // submitBtn.classList.add("btn--dark-lighter");
//         } else {
//           submitBtn.removeAttribute("disabled");
//           phoneField.classList.add("is-valid");
//           // submitBtn.classList.remove("btn--dark-lighter");
//         }
//       });
//   }
// });

// Verify Username Ajax Validation
usernameField.addEventListener("input", (e) => {
  const usernameVal = e.target.value;

  usernameSuccessOutput.style.display = "block";

  usernameSuccessOutput.innerHTML = '<i class="bi bi-arrow-repeat"></i>  '+`Checking  ${usernameVal}`;

  usernameField.classList.remove("is-valid");
  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";

  if (usernameVal.length > 0) {
    fetch("/Auth/validate-username/", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        usernameSuccessOutput.style.display = "none";
        console.log("data", data);
        if (data.username_error) {
          submitBtn.disabled = true;
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p class="text-danger">${data.username_error}</p>`;
          // submitBtn.classList.add("btn--dark-lighter");
        } else {
          submitBtn.removeAttribute("disabled");
          usernameField.classList.add("is-valid");
          // submitBtn.classList.remove("btn--dark-lighter");
        }
      });
  }
});

// Verify Email Ajax Validation
emailField.addEventListener("focusout", (e) => {
  const emailVal = e.target.value;

  emailSuccessOutput.style.display = "block";

  emailSuccessOutput.innerHTML = '<i class="bi bi-arrow-repeat"></i>  '+`Checking  ${emailVal}`;

  emailField.classList.remove("is-valid");
  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/Auth/validate-email/", {
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
