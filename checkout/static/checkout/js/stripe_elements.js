// Get keys from template using JQuery, stripping the first and last characters to remove quotation marks
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);


// element styles 
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
}


// Create instance of Stripe
var stripe = Stripe(stripe_public_key);
// Use to create an instance of stripe elements
var elements = stripe.elements();
// use that to create a card element
var card = elements.create('card', {style: style});
// then mount the card element to the div in the checkout page
card.mount('#card-element');