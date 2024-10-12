

# CloudErrorBody

An error response from Kusto.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | An identifier for the error. Codes are invariant and are intended to be consumed programmatically. |  [optional] |
|**details** | [**List&lt;CloudErrorBody&gt;**](CloudErrorBody.md) | A list of additional details about the error. |  [optional] |
|**message** | **String** | A message describing the error, intended to be suitable for displaying in a user interface. |  [optional] |
|**target** | **String** | The target of the particular error. For example, the name of the property in error. |  [optional] |



