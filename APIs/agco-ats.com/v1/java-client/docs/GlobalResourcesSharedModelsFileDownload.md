

# GlobalResourcesSharedModelsFileDownload

A language used for string translations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**CRC** | **String** | The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file. |  |
|**contentType** | **String** | The type of file; sent as the content-type header. |  |
|**description** | **String** | The description of the file. |  |
|**id** | **String** | The Id of the file. |  [optional] |
|**isPublic** | **Boolean** | Indicates whether this file is available to the public for download. |  |
|**name** | **String** | The name of the file when downloaded. |  |
|**path** | **String** | The Path of the file. |  |
|**size** | **Long** | The size of the file in bytes. Null until assigned by server when marked as &#39;Available&#39;. Read Only |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Indicates the state of this file. Must be &#39;Created&#39; when created. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;Created&quot; |
| AVAILABLE | &quot;Available&quot; |
| REMOVED | &quot;Removed&quot; |



