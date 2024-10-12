# GooglePlayDeveloper.InappPurchase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumptionState** | **Number** | The consumption state of the inapp product. Possible values are:   - Yet to be consumed  - Consumed | [optional] 
**developerPayload** | **String** | A developer-specified string that contains supplemental information about an order. | [optional] 
**kind** | **String** | This kind represents an inappPurchase object in the androidpublisher service. | [optional] [default to &#39;androidpublisher#inappPurchase&#39;]
**orderId** | **String** | The order id associated with the purchase of the inapp product. | [optional] 
**purchaseState** | **Number** | The purchase state of the order. Possible values are:   - Purchased  - Canceled  - Pending | [optional] 
**purchaseTime** | **String** | The time the product was purchased, in milliseconds since the epoch (Jan 1, 1970). | [optional] 
**purchaseType** | **Number** | The type of purchase of the inapp product. This field is only set if this purchase was not made using the standard in-app billing flow. Possible values are:   - Test (i.e. purchased from a license testing account)  - Promo (i.e. purchased using a promo code)  - Rewarded (i.e. from watching a video ad instead of paying) | [optional] 


