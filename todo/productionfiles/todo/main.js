

const task_status_done = document.querySelectorAll('.done');
// const task_status_progressing = document.querySelectorAll('.progressing');


task_status_done.forEach(function (element){
    element.parentElement.classList.remove("table-dark");
    element.parentElement.classList.remove("table-primary");
    element.parentElement.classList.add("table-success");
    element.parentElement.style.webkitTextFillColor = "black";
    element.parentElement.style.backgroundColor = "#C8E4B2";
    // console.log("halo")
});

const theme = document.querySelector("#bs5theme");
// const csrfToken = document.cookie.split("=")[1]
const themes = document.querySelectorAll(".themebs5");



function switchTheme(themeUrl){
    let clicked_element =  event.target;
    themes.forEach(function(element){
    // console.log(element);
    element.classList.remove("bi-palette-fill");
    element.classList.add("bi-palette");
})
    clicked_element.classList.remove("bi-palette");
    clicked_element.classList.add("bi-palette-fill");

    theme.href = themeUrl;
    fetch('/set-theme/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: 'theme=' + encodeURIComponent(themeUrl)
    });
}

// function switchTheme(themeUrl) {
//     theme.href = themeUrl;
//
//     // Retrieve CSRF token from the cookie
//     var csrfToken = getCookie('csrftoken');
//
//     // Make the POST request
//     fetch('/set-theme/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded',
//             'X-CSRFToken': csrfToken
//         },
//         body: 'theme=' + encodeURIComponent(themeUrl)
//     });
// }



// Function to retrieve the CSRF token from the cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//priority stars


//
// const stars = document.querySelectorAll('.star');
// const clearPriority = document.querySelector("#clearPriority")
// let isClicked = false;
//
// stars.forEach(function (star_element, index) {
//   star_element.addEventListener('mouseover', function () {
//     // console.log(star_element, index);
//     if (!isClicked) {
//       for (let star = 0; star <= index; star++) {
//         stars[star].classList.remove('bi-star');
//         stars[star].classList.add('bi-star-fill');
//       }
//     }
//   });
//
//   star_element.addEventListener('click', function () {
//     isClicked = true;
//     for (let star = 0; star <= index; star++) {
//       stars[star].classList.add('bi-star-fill');
//       // stars[star].classList.add('bi-star');
//     }
//   });
//
//   star_element.addEventListener('mouseout', function () {
//     // console.log(star_element, index);
//     if (!isClicked) {
//       for (let star = 0; star <= index; star++) {
//         stars[star].classList.remove('bi-star-fill');
//         stars[star].classList.add('bi-star');
//       }
//     }
//   });
// });
//
//
// clearPriority.addEventListener("click", function(){
//   stars.forEach(function(star_element){
//     isClicked = false;
//     star_element.classList.remove('bi-star-fill');
//     star_element.classList.add('bi-star');
//   })
// })

//quote generator


const api_url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?"
const RandomQuote = document.querySelector(".random-quote");
const fetchQuote = document.querySelector(".fetch-quote");

let data;
async function getapi(url)
{
  const response = await fetch(url, {
      headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
      }

  });

  data = await response.json();
  // console.log(data);
  RandomQuote.textContent = data["quoteText"]
}


const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

  $.ajax({
    url: '/user_timezone/',
    type: 'POST',
    data: { timezone: userTimezone },
    headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
    success: function (response) {
      // Handle the server's response (if needed)
    }
  });

// console.log(userTimezone)


$(document).ready(function () {
    $('[data-bs-toggle="tooltip"]').tooltip();
});




const searchBar = document.querySelector(".search-bar");
const taskTitles = document.querySelectorAll(".task-title");
const taskTitlesHidden = document.querySelectorAll(".task-title-hidden");


searchBar.addEventListener("input", function (e){
    const query = this.value.toLowerCase();
    taskTitles.forEach(function (element, index){
        const titleHidden = taskTitlesHidden[index];
        if (titleHidden.textContent.toLowerCase().includes(query)){
            element.parentElement.classList.remove("d-none");
        }else{
            element.parentElement.classList.add("d-none");
        }
    })
})








