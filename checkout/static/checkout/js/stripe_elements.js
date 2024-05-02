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

// Get keys from template using JQuery, stripping the first and last characters to remove quotation marks
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Create instance of Stripe
var stripe = Stripe(stripePublicKey);
// Use to create an instance of stripe elements
var elements = stripe.elements();
// use that to create a card element
var card = elements.create('card', {style: style});
// then mount the card element to the div in the checkout page
card.mount('#card-element');


// Handle realtime validation errors on card element, displaying information to user
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // stop default action on 'submit'
    ev.preventDefault();
    // disable card element and submit button to stop multiple submissions
    card.update({ 'disabled': true });
    $('submit-button').attr('disabled', true);
    // call the confirm card payment method, 
    stripe.confirmCardPayment(clientSecret, { //  send card details to stripe 
        payment_method: {
            card: card,
        }
    }).then(function(result) {  //  then execute function on the result
        // if error, put error message into card error div, 
        //  and re-enable the submit button to allow user to fix the issue
        // otherwise, if the status of payment intent returns as 'succeeded', submit the form.
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <spam>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

