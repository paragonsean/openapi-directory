# GooglePlayAndroidDeveloperApi.VoidedPurchase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** | This kind represents a voided purchase object in the androidpublisher service. | [optional] 
**orderId** | **String** | The order id which uniquely identifies a one-time purchase, subscription purchase, or subscription renewal. | [optional] 
**purchaseTimeMillis** | **String** | The time at which the purchase was made, in milliseconds since the epoch (Jan 1, 1970). | [optional] 
**purchaseToken** | **String** | The token which uniquely identifies a one-time purchase or subscription. To uniquely identify subscription renewals use order_id (available starting from version 3 of the API). | [optional] 
**voidedReason** | **Number** | The reason why the purchase was voided, possible values are: 0. Other 1. Remorse 2. Not_received 3. Defective 4. Accidental_purchase 5. Fraud 6. Friendly_fraud 7. Chargeback | [optional] 
**voidedSource** | **Number** | The initiator of voided purchase, possible values are: 0. User 1. Developer 2. Google | [optional] 
**voidedTimeMillis** | **String** | The time at which the purchase was canceled/refunded/charged-back, in milliseconds since the epoch (Jan 1, 1970). | [optional] 


