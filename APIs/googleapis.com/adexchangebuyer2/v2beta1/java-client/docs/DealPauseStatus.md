

# DealPauseStatus

Tracks which parties (if any) have paused a deal. The deal is considered paused if either hasBuyerPaused or hasSellPaused is true.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buyerPauseReason** | **String** | The buyer&#39;s reason for pausing, if the buyer paused the deal. |  [optional] |
|**firstPausedBy** | [**FirstPausedByEnum**](#FirstPausedByEnum) | The role of the person who first paused this deal. |  [optional] |
|**hasBuyerPaused** | **Boolean** | True, if the buyer has paused the deal unilaterally. |  [optional] |
|**hasSellerPaused** | **Boolean** | True, if the seller has paused the deal unilaterally. |  [optional] |
|**sellerPauseReason** | **String** | The seller&#39;s reason for pausing, if the seller paused the deal. |  [optional] |



## Enum: FirstPausedByEnum

| Name | Value |
|---- | -----|
| BUYER_SELLER_ROLE_UNSPECIFIED | &quot;BUYER_SELLER_ROLE_UNSPECIFIED&quot; |
| BUYER | &quot;BUYER&quot; |
| SELLER | &quot;SELLER&quot; |



