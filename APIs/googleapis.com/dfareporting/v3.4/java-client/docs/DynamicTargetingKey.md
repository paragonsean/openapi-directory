

# DynamicTargetingKey

Contains properties of a dynamic targeting key. Dynamic targeting keys are unique, user-friendly labels, created at the advertiser level in DCM, that can be assigned to ads, creatives, and placements and used for targeting with Studio dynamic creatives. Use these labels instead of numeric Campaign Manager IDs (such as placement IDs) to save time and avoid errors in your dynamic feeds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#dynamicTargetingKey\&quot;. |  [optional] |
|**name** | **String** | Name of this dynamic targeting key. This is a required field. Must be less than 256 characters long and cannot contain commas. All characters are converted to lowercase. |  [optional] |
|**objectId** | **String** | ID of the object of this dynamic targeting key. This is a required field. |  [optional] |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | Type of the object of this dynamic targeting key. This is a required field. |  [optional] |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| ADVERTISER | &quot;OBJECT_ADVERTISER&quot; |
| AD | &quot;OBJECT_AD&quot; |
| CREATIVE | &quot;OBJECT_CREATIVE&quot; |
| PLACEMENT | &quot;OBJECT_PLACEMENT&quot; |



