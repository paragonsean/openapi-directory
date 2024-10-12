# GoogleMyBusinessApi.ListAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**[Account]**](Account.md) | A collection of accounts to which the user has access. The personal account of the user doing the query will always be the first item of the result, unless it is filtered out. | [optional] 
**nextPageToken** | **String** | If the number of accounts exceeds the requested page size, this field is populated with a token to fetch the next page of accounts on a subsequent call to &#x60;accounts.list&#x60;. If there are no more accounts, this field is not present in the response. | [optional] 


