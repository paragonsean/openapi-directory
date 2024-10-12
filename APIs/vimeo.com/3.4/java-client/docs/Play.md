

# Play


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**progressive** | [**List&lt;PlayProgressiveInner&gt;**](PlayProgressiveInner.md) | Progressive files. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The play status of the video:  Option descriptions:  * &#x60;playable&#x60; - The video is playable.  * &#x60;purchase_required&#x60; - The video must be purchased.  * &#x60;restricted&#x60; - Playback for the video is restricted.  * &#x60;unavailable&#x60; - The video is unavailable.  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PLAYABLE | &quot;playable&quot; |
| PURCHASE_REQUIRED | &quot;purchase_required&quot; |
| RESTRICTED | &quot;restricted&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



