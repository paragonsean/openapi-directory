

# ListBankAccountsResponse

Response object returned by ListBankAccounts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccounts** | [**List&lt;BankAccount&gt;**](BankAccount.md) | List of BankAccounts associated with this account. |  [optional] |
|**cursor** | **String** | When a response is truncated, it includes a cursor that you can  use in a subsequent request to fetch next set of bank accounts. If empty, this is the final response.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information on errors encountered during the request. |  [optional] |



