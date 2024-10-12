

# OperationListResult

Result of the request to list REST API operations. It contains a list of operations and a URL nextLink to get the next set of results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | URL to get the next set of operation list results if there are any. |  [optional] [readonly] |
|**value** | [**List&lt;Operation&gt;**](Operation.md) | List of operations supported by the resource provider. |  [optional] |



