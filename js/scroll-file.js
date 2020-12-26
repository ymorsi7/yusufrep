/*jslint devel: true */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undef */
/*eslint-env es6*/
/*exported showAlert()*/
/* eslint-disable no-console */



// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myFunction1()};

function myFunction1() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";
}    