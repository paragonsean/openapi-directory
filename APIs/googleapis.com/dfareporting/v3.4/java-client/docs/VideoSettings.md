

# VideoSettings

Video Settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**companionSettings** | [**CompanionSetting**](CompanionSetting.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#videoSettings\&quot;. |  [optional] |
|**obaEnabled** | **Boolean** | Whether OBA icons are enabled for this placement. |  [optional] |
|**obaSettings** | [**ObaIcon**](ObaIcon.md) |  |  [optional] |
|**orientation** | [**OrientationEnum**](#OrientationEnum) | Orientation of a video placement. If this value is set, placement will return assets matching the specified orientation. |  [optional] |
|**skippableSettings** | [**SkippableSetting**](SkippableSetting.md) |  |  [optional] |
|**transcodeSettings** | [**TranscodeSetting**](TranscodeSetting.md) |  |  [optional] |



## Enum: OrientationEnum

| Name | Value |
|---- | -----|
| ANY | &quot;ANY&quot; |
| LANDSCAPE | &quot;LANDSCAPE&quot; |
| PORTRAIT | &quot;PORTRAIT&quot; |



