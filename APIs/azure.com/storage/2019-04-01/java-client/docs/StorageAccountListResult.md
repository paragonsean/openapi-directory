

# StorageAccountListResult

The response from the List Storage Accounts operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | Request URL that can be used to query next page of storage accounts. Returned when total number of requested storage accounts exceed maximum page size. |  [optional] [readonly] |
|**value** | [**List&lt;StorageAccount&gt;**](StorageAccount.md) | Gets the list of storage accounts and their properties. |  [optional] [readonly] |



