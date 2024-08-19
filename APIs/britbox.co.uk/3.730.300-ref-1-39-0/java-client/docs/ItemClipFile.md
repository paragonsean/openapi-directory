

# ItemClipFile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channels** | **Integer** | The number of audio channels. |  [optional] |
|**deliveryType** | [**DeliveryTypeEnum**](#DeliveryTypeEnum) | The way in which the media file is delivered. |  |
|**drm** | **String** | The type of drm used to encrypt the media. &#39;None&#39; if unencrypted. |  |
|**format** | **String** | The format the media was encoded in. |  |
|**height** | **Integer** | The height of the video media. |  |
|**language** | **String** | The language code for the media, e.g. &#39;en&#39;. |  |
|**name** | **String** | The name of the media file. |  |
|**resolution** | [**ResolutionEnum**](#ResolutionEnum) | The resolution of the video media. |  |
|**url** | **URI** | The url to access the media file. |  |
|**width** | **Integer** | The width of the video media. |  |



## Enum: DeliveryTypeEnum

| Name | Value |
|---- | -----|
| STREAM | &quot;Stream&quot; |
| PROGRESSIVE | &quot;Progressive&quot; |
| DOWNLOAD | &quot;Download&quot; |



## Enum: ResolutionEnum

| Name | Value |
|---- | -----|
| SD | &quot;SD&quot; |
| HD_720 | &quot;HD-720&quot; |
| HD_1080 | &quot;HD-1080&quot; |
| HD_4_K | &quot;HD-4K&quot; |
| EXTERNAL | &quot;External&quot; |
| UNKNOWN | &quot;Unknown&quot; |



