

# CloudErrorBody

The object that defines the structure of an Azure Data Factory error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Error code. |  |
|**details** | [**List&lt;CloudError&gt;**](CloudError.md) | Array with additional error details. |  [optional] |
|**message** | **String** | Error message. |  |
|**target** | **String** | Property name/path in request associated with error. |  [optional] |



