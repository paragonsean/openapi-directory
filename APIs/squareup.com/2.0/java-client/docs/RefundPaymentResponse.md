

# RefundPaymentResponse

Defines the response returned by  [RefundPayment](https://developer.squareup.com/reference/square_2021-08-18/refunds-api/refund-payment).  If there are errors processing the request, the `refund` field might not be present, or it might be present with a status of `FAILED`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |
|**refund** | [**PaymentRefund**](PaymentRefund.md) |  |  [optional] |



