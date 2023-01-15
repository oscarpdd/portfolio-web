// Set variables to calculate the footer line width.
const numFooterLinks = $('.bi-personal-link').length;

//const images_width = num_footer_links * num + unit;
let imagesWidth = numFooterLinks * document.querySelector('.bi-personal-link').offsetWidth + 'px';
let footerWidth = document.querySelector('.footer-section').offsetWidth;
let footerLineWidthCalc = '(' + footerWidth.toString() + 'px -  ' + imagesWidth + ') / 2'
let footerLineWidth = 'calc(0.9 * ' + footerLineWidthCalc + ')';

/*
Set the variable "footer line width" on the footer as a property.
This means that we can access to that property as a variable on CSS.
 */
let footerStyle = document.querySelector('.footer-section').style;
footerStyle.setProperty('--footer-line-width', footerLineWidth);

// Set variables to calculate the Footer Height.
let footerHeight = document.querySelector('.footer-section').offsetHeight;
let footerLineBias = 'calc(' + Math.trunc(footerHeight / 2).toString() + 'px - 0.2em)';

// Set the variable "footer height" to use it on the CSS.
footerStyle.setProperty('--footer-line-height-position', footerLineBias);

// Change screen properties on resize.
window.onresize = function() {
    // Calculate the footer line width.
    imagesWidth = numFooterLinks * document.querySelector('.bi-personal-link').offsetWidth + 'px';
    footerWidth = document.querySelector('.footer').offsetWidth;
    footerLineWidthCalc = '(' + footerWidth.toString() + 'px -  ' + imagesWidth + ') / 2'
    footerLineWidth = 'calc(0.9 * ' + footerLineWidthCalc + ')';

    /*
    Set the variable "footer line width" on the footer as a property.
    This means that we can access to that property as a variable on CSS.
     */
    footerStyle = document.querySelector('.footer-section').style;
    footerStyle.setProperty('--footer-line-width', footerLineWidth);

    // Set variables to calculate the Footer Height.
    footerHeight = document.querySelector('.footer-section').offsetHeight;
    footerLineBias = 'calc(' + Math.trunc(footerHeight / 2).toString() + 'px - 0.2em)';

    // Set the variable "footer height" to use it on the CSS.
    footerStyle.setProperty('--footer-line-height-position', footerLineBias);
}
