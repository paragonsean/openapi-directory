

# CreateVideoVersionRequestUpload


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approach** | [**ApproachEnum**](#ApproachEnum) | Upload approach |  |
|**link** | **String** | If your upload approach is pull, Vimeo will download the video hosted at this public URL. This URL must be valid for at least 24 hours. |  [optional] |
|**redirectUrl** | **String** | The app&#39;s redirect URL. Use this parameter when &#x60;approach&#x60; is &#x60;post&#x60;. |  [optional] |
|**size** | **String** | Upload size |  [optional] |



## Enum: ApproachEnum

| Name | Value |
|---- | -----|
| POST | &quot;post&quot; |
| PULL | &quot;pull&quot; |
| STREAMING | &quot;streaming&quot; |
| TUS | &quot;tus&quot; |



