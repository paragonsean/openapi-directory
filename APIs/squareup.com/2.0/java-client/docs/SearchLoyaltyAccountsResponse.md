

# SearchLoyaltyAccountsResponse

A response that includes loyalty accounts that satisfy the search criteria.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to use in a subsequent  request. If empty, this is the final response. For more information,  see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**loyaltyAccounts** | [**List&lt;LoyaltyAccount&gt;**](LoyaltyAccount.md) | The loyalty accounts that met the search criteria,   in order of creation date. |  [optional] |



