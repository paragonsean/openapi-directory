

# OperationListResult

Result of the request to list ServiceFabric operations. It contains a list of operations and a URL link to get the next set of results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | URL to get the next set of operation list results if there are any. |  [optional] [readonly] |
|**value** | [**List&lt;OperationResult&gt;**](OperationResult.md) | List of ServiceFabric operations supported by the Microsoft.ServiceFabric resource provider. |  [optional] [readonly] |



