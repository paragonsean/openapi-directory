# AuthorizedBuyersMarketplaceApi.FinalizedDeal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal** | [**Deal**](Deal.md) |  | [optional] 
**dealPausingInfo** | [**DealPausingInfo**](DealPausingInfo.md) |  | [optional] 
**dealServingStatus** | **String** | Serving status of the deal. | [optional] 
**name** | **String** | The resource name of the finalized deal. Format: &#x60;buyers/{accountId}/finalizedDeals/{finalizedDealId}&#x60; | [optional] 
**readyToServe** | **Boolean** | Whether the Programmatic Guaranteed deal is ready for serving. | [optional] 
**rtbMetrics** | [**RtbMetrics**](RtbMetrics.md) |  | [optional] 



## Enum: DealServingStatusEnum


* `DEAL_SERVING_STATUS_UNSPECIFIED` (value: `"DEAL_SERVING_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `ENDED` (value: `"ENDED"`)

* `PAUSED_BY_BUYER` (value: `"PAUSED_BY_BUYER"`)

* `PAUSED_BY_SELLER` (value: `"PAUSED_BY_SELLER"`)




