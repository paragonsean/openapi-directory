

# ListOperationsResponse

ListOperationsResponse is the result of ListOperationsRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**missingZones** | **List&lt;String&gt;** | If any zones are listed here, the list of operations returned may be missing the operations from those zones. |  [optional] |
|**operations** | [**List&lt;Operation&gt;**](Operation.md) | A list of operations in the project in the specified zone. |  [optional] |



