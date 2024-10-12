

# PayOrderRequest

Defines the fields that are included in requests to the [PayOrder](https://developer.squareup.com/reference/square_2021-08-18/orders-api/pay-order) endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**idempotencyKey** | **String** | A value you specify that uniquely identifies this request among requests you have sent. If you are unsure whether a particular payment request was completed successfully, you can reattempt it with the same idempotency key without worrying about duplicate payments.  For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency). |  |
|**orderVersion** | **Integer** | The version of the order being paid. If not supplied, the latest version will be paid. |  [optional] |
|**paymentIds** | **List&lt;String&gt;** | The IDs of the [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) to collect. The payment total must match the order total. |  [optional] |



