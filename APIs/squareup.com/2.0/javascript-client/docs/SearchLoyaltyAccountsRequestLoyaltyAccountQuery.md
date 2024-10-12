# SquareConnectApi.SearchLoyaltyAccountsRequestLoyaltyAccountQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerIds** | **[String]** | The set of customer IDs to use in the loyalty account search.    This cannot be combined with &#x60;mappings&#x60;.    Max: 30 customer IDs | [optional] 
**mappings** | [**[LoyaltyAccountMapping]**](LoyaltyAccountMapping.md) | The set of mappings to use in the loyalty account search.    This cannot be combined with &#x60;customer_ids&#x60;.    Max: 30 mappings | [optional] 


