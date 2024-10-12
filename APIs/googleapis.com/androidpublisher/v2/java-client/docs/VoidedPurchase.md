

# VoidedPurchase

A VoidedPurchase resource indicates a purchase that was either canceled/refunded/charged-back.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | This kind represents a voided purchase object in the androidpublisher service. |  [optional] |
|**purchaseTimeMillis** | **String** | The time at which the purchase was made, in milliseconds since the epoch (Jan 1, 1970). |  [optional] |
|**purchaseToken** | **String** | The token which uniquely identifies a one-time purchase or subscription. To uniquely identify subscription renewals use order_id (available starting from version 3 of the API). |  [optional] |
|**voidedTimeMillis** | **String** | The time at which the purchase was canceled/refunded/charged-back, in milliseconds since the epoch (Jan 1, 1970). |  [optional] |



