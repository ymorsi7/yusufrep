/*jslint devel: true */
/* eslint-disable no-unused-vars */
/* eslint-disable no-undef */
/*eslint-env es6*/
/*exported showAlert()*/
/* eslint-disable no-console */


let visitingWebsite = true;
let notVistingWebsite = false;

if (visitingWebsite){
    alert('Welcome to my Portfolio!');
} else {
    alert('Visit my Portfolio!')
}
 /* Above is an if else statement and boolean logic, and below is a function and arthimatic */


/* For inserting elements */

function insertFunc1() {
    var elementToBeAddedTo = document.getElementById("AddToThisElement");
    elementToBeAddedTo.insertAdjacentHTML('afterend', '<p>My email is already above 😂 However, in case you removed it, it is ymorsi8@gmail.com</p>')}

function insertFunc2() {
    var elementToBeAddedTo = document.getElementById("AddToThisElement");
    elementToBeAddedTo.insertAdjacentHTML('afterend', '<section>All the projects that I spend large amounts of time on can be found here. This page will be updated regularly, so stay tuned!</section>')}

function insertFunc3() {
    var elementToBeAddedTo = document.getElementById("AddToThisElement");
    elementToBeAddedTo.insertAdjacentHTML('afterend', '<div>To learn more about me, visit my LinkedIn page!</div>')}

function removioli() {
    var elementToRemove = document.getElementById("RemoveThisParagraph");
    elementToRemove.remove();}

function removiolidiv() {
    var elementToRemove = document.getElementById("RemoveThisDiv");
    elementToRemove.remove();}

function removiolisection() {
    var elementToRemove = document.getElementById("RemoveThisSection");
    elementToRemove.remove();}

function changeToBlue() {
	document.getElementById("sampletext").style.color = "blue";
}

function changeText(){
	document.getElementById("sampletext").innerHTML = "Surpassing Photography Instagram Posts";}
    
function changeToRed() {
    document.getElementById("waldo").style.color = "red";}

function uppercase() {
    document.getElementById("myP").style.textTransform = "capitalize";}
    
    
function attChange() {
    document.getElementById("sampletext").className = "p.blue";}

function attyChange() {
    document.getElementById("myP").className = "blue";}

var vplaces = ["San Diego, CA", " Los Angeles, CA ", " San Francisco, CA", " Sacramento, CA", " Las Vegas, NV", "       Cairo, Egypt", " Phoenix, AZ", " Yuma, AZ", " Alexandria, Egypt", " Instanbul, Turkey", " Jeddah, Saudi Arabia",     " Anaheim, CA"];
    document.getElementById("places").innerHTML = vplaces;

var var2 = ["Some things that I like to do in my free time include:"];
                    document.getElementById("var2").innerHTML = var2;
    
var var3 = [" I created this website as part of an assignment for my UCSD Extension Front-End Web Development course. In this website, I wrote a bit about myself, listed many of my projects (on this page), uploaded my photos to a Photography page, and more. Below is a screenshot of the home page of my portfolio on July 1<sup>st</sup> 2020. "];
                    document.getElementById("var3").innerHTML = var3;

var var4 = [" In this fun experience, I toured multiple build sites in San Francisco and Sacramento, went on several Architectural, Construction, and Engineering job walks in Sacramento, and did much more! The camp was 6 days long (we slept five nights in a dorm at CSU Sacramento), and before leaving for the airport on the last day, my group and I presented a slideshow that we created the previous day about what we learned on the trip at SRBX. "];
                    document.getElementById("var4").innerHTML = var4;

var var5 = [" This is a commercial design project that I worked on in my Honors PLTW Civil Engineering and Architecture (1,2) course in high school. Below is a slideshow compiling the key elements of the project in addition to a site plan, electrical plans, and a few renderings. "];
                    document.getElementById("var5").innerHTML = var5;

    