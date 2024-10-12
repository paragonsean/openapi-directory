

# SearchLoyaltyAccountsRequestLoyaltyAccountQuery

The search criteria for the loyalty accounts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerIds** | **List&lt;String&gt;** | The set of customer IDs to use in the loyalty account search.    This cannot be combined with &#x60;mappings&#x60;.    Max: 30 customer IDs |  [optional] |
|**mappings** | [**List&lt;LoyaltyAccountMapping&gt;**](LoyaltyAccountMapping.md) | The set of mappings to use in the loyalty account search.    This cannot be combined with &#x60;customer_ids&#x60;.    Max: 30 mappings |  [optional] |



