

# PresentationParams

Hints for displaying the asset, based on information available when the asset was uploaded.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backgroundColor** | **String** | A background color which could be used for displaying the 3D asset in a &#39;thumbnail&#39; or &#39;palette&#39; style view. Authors have the option to set this background color when publishing or editing their asset. This is represented as a six-digit hexademical triplet specifying the RGB components of the background color, e.g. #FF0000 for Red. |  [optional] |
|**colorSpace** | [**ColorSpaceEnum**](#ColorSpaceEnum) | The materials&#39; diffuse/albedo color. This does not apply to vertex colors or texture maps. |  [optional] |
|**orientingRotation** | [**Quaternion**](Quaternion.md) |  |  [optional] |



## Enum: ColorSpaceEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| LINEAR | &quot;LINEAR&quot; |
| GAMMA | &quot;GAMMA&quot; |



