

# UpdatePaymentRequest

Describes a request to update a payment using  [UpdatePayment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/update-payment).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**idempotencyKey** | **String** | A unique string that identifies this &#x60;UpdatePayment&#x60; request. Keys can be any valid string but must be unique for every &#x60;UpdatePayment&#x60; request.  The maximum is 45 characters.  For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency). |  |
|**payment** | [**Payment**](Payment.md) |  |  [optional] |



