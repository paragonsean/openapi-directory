

# BatchError

An error response received from the Azure Batch service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Gets or sets an identifier for the error. Codes are invariant and are intended to be consumed programmatically. |  [optional] |
|**message** | [**ErrorMessage**](ErrorMessage.md) |  |  [optional] |
|**values** | [**List&lt;BatchErrorDetail&gt;**](BatchErrorDetail.md) | Gets or sets a collection of key-value pairs containing additional details about the error. |  [optional] |



