   /**
 * Globals
 */
   const OPERATIONS = ['add', 'subtract', 'divide', 'multiply', 'modulus', 'sqrt', 'mod', 'power'];
   const OPERATION_SYMBOLS = {
     add: '+',
     subtract: '-',
     divide: '/',
     multiply: '*',
     modulus: '%',
     sqrt: '√',
     mod: '‰',
     power: '^',
   };
   
   const OPERATION_REGEX = /[-+*/%√^‰]/g;
   const REST_URL = 'http://127.0.0.1:5000/calculator';
   
   // Calculator Logic
   const display = document.getElementById('display');
   
   let operation = '';
   
   function appendValue(value) {
     if (OPERATIONS.includes(value)) {
       operation = value;
       display.value += OPERATION_SYMBOLS[value];
       return;
     }
   
     display.value += value;
   }
   
   function clearDisplay() {
     display.value = '';
     operation = '';
   }
   
   function calculateResult() {
     const nums = display.value.split(OPERATION_REGEX);
     const url = composeUrl(nums, operation);
     fetch(url)
       .then((res) => {
         if (!res.ok) {
           return Promise.reject(res);
         }
         return res.json();
       })
       .then((data) => {
         display.value = data.sum;
       })
       .catch((err) => {
         err.json().then((error) => {
           display.value = error.error;
         });
       });
   }
   
   function composeUrl(nums, operation) {
     let finalUrl = `${REST_URL}/${operation}?`;
     nums.forEach((num, index) => {
       finalUrl = `${finalUrl}num${index + 1}=${num}`;
       if (index !== nums.length - 1) {
         finalUrl = `${finalUrl}&`;
       }
     });
   
     return finalUrl;
   }
   