

# OperationListResult

Result of the request to list Windows IoT Device Service operations. It contains a list of operations and a URL link to get the next set of results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | URL to get the next set of operation list results if there are any. |  [optional] [readonly] |
|**value** | [**List&lt;OperationEntity&gt;**](OperationEntity.md) | List of Windows IoT Device Service operations supported by the Microsoft.WindowsIoT resource provider. |  [optional] [readonly] |



