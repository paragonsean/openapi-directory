

# DealServingMetadataDealPauseStatus

Tracks which parties (if any) have paused a deal. The deal is considered paused if has_buyer_paused || has_seller_paused. Each of the has_buyer_paused or the has_seller_paused bits can be set independently.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buyerPauseReason** | **String** |  |  [optional] |
|**firstPausedBy** | **String** | If the deal is paused, records which party paused the deal first. |  [optional] |
|**hasBuyerPaused** | **Boolean** |  |  [optional] |
|**hasSellerPaused** | **Boolean** |  |  [optional] |
|**sellerPauseReason** | **String** |  |  [optional] |



