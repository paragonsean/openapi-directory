

# Picture


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether this picture is the active picture for its parent resource. |  |
|**link** | **String** | The upload URL for the picture. This field appears when you create the picture resource for the first time. |  [optional] |
|**resourceKey** | **String** | The picture&#39;s resource key string. |  |
|**sizes** | [**List&lt;PictureSizesInner&gt;**](PictureSizesInner.md) | An array containing reference information about all available image files. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the picture:  Option descriptions:  * &#x60;caution&#x60; - An image that is appropriate for all ages.  * &#x60;custom&#x60; - A custom image for the video.  * &#x60;default&#x60; - The default image for the video.  |  |
|**uri** | **String** | The picture&#39;s URI. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAUTION | &quot;caution&quot; |
| CUSTOM | &quot;custom&quot; |
| DEFAULT | &quot;default&quot; |



