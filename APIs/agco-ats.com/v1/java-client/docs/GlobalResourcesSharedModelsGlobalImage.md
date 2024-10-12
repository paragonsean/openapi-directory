

# GlobalResourcesSharedModelsGlobalImage

An image from the Global Image library.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**CRC** | **String** | The Hash of the file (SHA256, HEX-encoded). |  |
|**categories** | [**List&lt;GlobalResourcesSharedModelsGlobalImageCategory&gt;**](GlobalResourcesSharedModelsGlobalImageCategory.md) | The category of the file. |  [optional] |
|**date** | **OffsetDateTime** | The date of the file. |  [optional] |
|**description** | **String** | The description of the file. |  |
|**height** | **Integer** | The height of the file. |  |
|**id** | **String** | The Id of the GlobalImage Metadata. |  [optional] |
|**name** | **String** | The name of the file when downloaded. |  |
|**publisher** | **String** | The Publisher of the file. |  [optional] |
|**size** | **Long** | The size of the file in bytes. Null until assigned by server when marked as &#39;Available&#39;. Read Only |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Indicates the state of this file. Must be &#39;Created&#39; when created. Read Only. |  |
|**thumbnailCRC** | **String** | The Hash of the thumbnail file (SHA256, HEX-encoded). |  |
|**thumbnailSize** | **Long** | The size of the thumbnail file in bytes. Null until assigned by server when marked as &#39;Available&#39;. Read Only |  [optional] |
|**width** | **Integer** | The width of the file. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;Created&quot; |
| AVAILABLE | &quot;Available&quot; |
| REMOVED | &quot;Removed&quot; |



