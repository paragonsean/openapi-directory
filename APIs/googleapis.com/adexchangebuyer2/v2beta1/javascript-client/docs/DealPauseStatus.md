# AdExchangeBuyerApiIi.DealPauseStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyerPauseReason** | **String** | The buyer&#39;s reason for pausing, if the buyer paused the deal. | [optional] 
**firstPausedBy** | **String** | The role of the person who first paused this deal. | [optional] 
**hasBuyerPaused** | **Boolean** | True, if the buyer has paused the deal unilaterally. | [optional] 
**hasSellerPaused** | **Boolean** | True, if the seller has paused the deal unilaterally. | [optional] 
**sellerPauseReason** | **String** | The seller&#39;s reason for pausing, if the seller paused the deal. | [optional] 



## Enum: FirstPausedByEnum


* `BUYER_SELLER_ROLE_UNSPECIFIED` (value: `"BUYER_SELLER_ROLE_UNSPECIFIED"`)

* `BUYER` (value: `"BUYER"`)

* `SELLER` (value: `"SELLER"`)




