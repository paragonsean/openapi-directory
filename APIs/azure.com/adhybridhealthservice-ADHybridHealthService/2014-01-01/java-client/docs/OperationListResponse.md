

# OperationListResponse

Lists all of the available REST API operations for Azure Active Directory Connect Health.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuationToken** | **String** | The continuation token to get next set of operations. |  [optional] |
|**nextLink** | **String** | URL to get the next set of operation list results if there are any. |  [optional] [readonly] |
|**totalCount** | **Integer** | The total count of operations. |  [optional] |
|**value** | [**List&lt;Operation&gt;**](Operation.md) | List of operations supported by the Microsoft.ADHybridHealthService resource provider. |  [optional] [readonly] |



