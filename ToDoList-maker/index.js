const URL = 'http://127.0.0.1:5500';
const Endpoints = {
  authorization: '/todolist/authorization',
};
let isAuthorized = false;

const authForm = document.querySelector('[data-authorization-form]');

authForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const formData = new FormData(authForm);
  const values = { username: formData.get('username'), password: formData.get('password') };

  fetch(`${URL}${Endpoints.authorization}`, {
    method: 'Post',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(values),
  })
    .then((res) => res.json())
    .then((data) => {
      debugger;
    })
    .catch((err) => {
      console.log(err);
    });
});
