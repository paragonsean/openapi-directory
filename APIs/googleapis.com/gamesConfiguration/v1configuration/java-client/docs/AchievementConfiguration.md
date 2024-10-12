

# AchievementConfiguration

An achievement configuration resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**achievementType** | [**AchievementTypeEnum**](#AchievementTypeEnum) | The type of the achievement. |  [optional] |
|**draft** | [**AchievementConfigurationDetail**](AchievementConfigurationDetail.md) |  |  [optional] |
|**id** | **String** | The ID of the achievement. |  [optional] |
|**initialState** | [**InitialStateEnum**](#InitialStateEnum) | The initial state of the achievement. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;gamesConfiguration#achievementConfiguration&#x60;. |  [optional] |
|**published** | [**AchievementConfigurationDetail**](AchievementConfigurationDetail.md) |  |  [optional] |
|**stepsToUnlock** | **Integer** | Steps to unlock. Only applicable to incremental achievements. |  [optional] |
|**token** | **String** | The token for this resource. |  [optional] |



## Enum: AchievementTypeEnum

| Name | Value |
|---- | -----|
| ACHIEVEMENT_TYPE_UNSPECIFIED | &quot;ACHIEVEMENT_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| INCREMENTAL | &quot;INCREMENTAL&quot; |



## Enum: InitialStateEnum

| Name | Value |
|---- | -----|
| INITIAL_STATE_UNSPECIFIED | &quot;INITIAL_STATE_UNSPECIFIED&quot; |
| HIDDEN | &quot;HIDDEN&quot; |
| REVEALED | &quot;REVEALED&quot; |



