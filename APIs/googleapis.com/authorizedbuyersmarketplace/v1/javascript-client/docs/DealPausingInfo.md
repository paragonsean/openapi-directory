# AuthorizedBuyersMarketplaceApi.DealPausingInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pauseReason** | **String** | The reason for the pausing of the deal; empty for active deals. | [optional] 
**pauseRole** | **String** | The party that first paused the deal; unspecified for active deals. | [optional] 
**pausingConsented** | **Boolean** | Whether pausing is consented between buyer and seller for the deal. | [optional] 



## Enum: PauseRoleEnum


* `BUYER_SELLER_ROLE_UNSPECIFIED` (value: `"BUYER_SELLER_ROLE_UNSPECIFIED"`)

* `BUYER` (value: `"BUYER"`)

* `SELLER` (value: `"SELLER"`)




