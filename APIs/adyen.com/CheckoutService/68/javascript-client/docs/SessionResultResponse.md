# AdyenCheckoutApi.SessionResultResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | A unique identifier of the session. | [optional] 
**status** | **String** | The status of the session. The status included in the response doesn&#39;t get updated. Don&#39;t make the request again to check for payment status updates.  Possible values:           * **completed** – The shopper completed the payment. This means that the payment was authorized.          * **paymentPending** – The shopper is in the process of making the payment. This applies to payment methods with an asynchronous flow.          * **refused** – The session has been refused, due to too many refused payment attempts. Shoppers can no longer complete the payment with this session.          * **canceled** – The shopper canceled the payment.          * **active** – The session is still active and can be paid.          * **expired** – The session expired (default: 1 hour after session creation). Shoppers can no longer complete the payment with this session.  | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `canceled` (value: `"canceled"`)

* `completed` (value: `"completed"`)

* `expired` (value: `"expired"`)

* `paymentPending` (value: `"paymentPending"`)

* `refused` (value: `"refused"`)




