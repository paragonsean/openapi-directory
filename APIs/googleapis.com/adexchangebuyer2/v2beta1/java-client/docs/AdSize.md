

# AdSize

Represents size of a single ad slot, or a creative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**height** | **String** | The height of the ad slot in pixels. This field will be present only when size type is &#x60;PIXEL&#x60;. |  [optional] |
|**sizeType** | [**SizeTypeEnum**](#SizeTypeEnum) | The size type of the ad slot. |  [optional] |
|**width** | **String** | The width of the ad slot in pixels. This field will be present only when size type is &#x60;PIXEL&#x60;. |  [optional] |



## Enum: SizeTypeEnum

| Name | Value |
|---- | -----|
| SIZE_TYPE_UNSPECIFIED | &quot;SIZE_TYPE_UNSPECIFIED&quot; |
| PIXEL | &quot;PIXEL&quot; |
| INTERSTITIAL | &quot;INTERSTITIAL&quot; |
| NATIVE | &quot;NATIVE&quot; |
| FLUID | &quot;FLUID&quot; |



