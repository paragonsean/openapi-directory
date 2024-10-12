

# GoogleAppsDriveLabelsV2LabelLock

A Lock that can be applied to a Label, Field, or Choice.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**GoogleAppsDriveLabelsV2LabelLockCapabilities**](GoogleAppsDriveLabelsV2LabelLockCapabilities.md) |  |  [optional] |
|**choiceId** | **String** | The ID of the Selection Field Choice that should be locked. If present, &#x60;field_id&#x60; must also be present. |  [optional] |
|**createTime** | **String** | Output only. The time this LabelLock was created. |  [optional] [readonly] |
|**creator** | [**GoogleAppsDriveLabelsV2UserInfo**](GoogleAppsDriveLabelsV2UserInfo.md) |  |  [optional] |
|**deleteTime** | **String** | Output only. A timestamp indicating when this LabelLock was scheduled for deletion. This will be present only if this LabelLock is in the DELETING state. |  [optional] [readonly] |
|**fieldId** | **String** | The ID of the Field that should be locked. Empty if the whole Label should be locked. |  [optional] |
|**name** | **String** | Output only. Resource name of this LabelLock. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. This LabelLock&#39;s state. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |



