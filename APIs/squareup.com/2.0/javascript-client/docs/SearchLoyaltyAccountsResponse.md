# SquareConnectApi.SearchLoyaltyAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | The pagination cursor to use in a subsequent  request. If empty, this is the final response. For more information,  see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] 
**errors** | [**[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**loyaltyAccounts** | [**[LoyaltyAccount]**](LoyaltyAccount.md) | The loyalty accounts that met the search criteria,   in order of creation date. | [optional] 


