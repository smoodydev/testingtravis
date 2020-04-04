// To get payments to work, we need to write some javascript. And this is the JavaScript code that's required by Stripe's API. And as you can see, it's all, in fact, jQuery rather than native JavaScript ($). And this just links up our HTML forms, our Django forms, to Stripe's API, which is in JavaScript.

// And you can see here, the Stripe API has given us a number of IDs that we can then use within our own code. So if we want to display the credit card errors, it's given us an ID there that we can use. So all of this code is not our own code. This is code that we get from Stripe's API developer site. And you have to stick to these IDs. You can't just write whatever you'd like. This is what's required in order for the Stripe API to work. Now we just add #errors. That's an ID.

// This is code that we get from Stripe's API developer site. Have a look

$(function() {
  $('#payment-form').submit(function() {
    var form = this;
    var card = {
      number: $('#id_credit_card_number').val(),
      expMonth: $('#id_expiry_month').val(),
      expYear: $('#id_expiry-year').val(),
      cvc: $('#id_cvv').val()
    };

  Stripe.createToken(card, function(status, response) {
    if (status == 200) {
      $('#credit-card-errors').hide();
      $('#id_stripe_id').val(response.id);

      // Prevent the Credit card details from being submitted to our server
      $('#id_credit_card_number').removeAttr('name');
      $('#id_cvv').removeAttr('name');
      $('#id_expiry_month').removeAttr('name');
      $('#id_expiry_year').removeAttr('name');

      form.submit();

    } else {
      $('#stripe-error-message').text(response.error.message);
      $('#credit-card-errors').show();
      $('#validate_card_btn').attr('disabled', false)
    }
  });
  return false;
  })
})




