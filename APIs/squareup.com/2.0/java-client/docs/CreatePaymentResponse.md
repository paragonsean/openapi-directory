

# CreatePaymentResponse

Defines the response returned by [CreatePayment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/create-payment).  If there are errors processing the request, the `payment` field might not be present, or it might be present with a status of `FAILED`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |
|**payment** | [**Payment**](Payment.md) |  |  [optional] |



