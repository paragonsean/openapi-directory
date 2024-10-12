

# InvoiceCreateAttachmentApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**link** | **String** | Link to the file |  [optional] |
|**obfuscatedFileName** | **String** | Hashed file name to avoid url wildguessing |  [optional] |
|**originalFileName** | **String** | Name of the file |  [optional] |
|**size** | **Long** | File size number in bytes |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the link (Attached or external) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EXTERNAL | &quot;External&quot; |
| UPLOADED | &quot;Uploaded&quot; |



