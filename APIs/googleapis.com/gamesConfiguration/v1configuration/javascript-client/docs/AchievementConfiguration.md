# GooglePlayGameServicesPublishingApi.AchievementConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievementType** | **String** | The type of the achievement. | [optional] 
**draft** | [**AchievementConfigurationDetail**](AchievementConfigurationDetail.md) |  | [optional] 
**id** | **String** | The ID of the achievement. | [optional] 
**initialState** | **String** | The initial state of the achievement. | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;gamesConfiguration#achievementConfiguration&#x60;. | [optional] 
**published** | [**AchievementConfigurationDetail**](AchievementConfigurationDetail.md) |  | [optional] 
**stepsToUnlock** | **Number** | Steps to unlock. Only applicable to incremental achievements. | [optional] 
**token** | **String** | The token for this resource. | [optional] 



## Enum: AchievementTypeEnum


* `ACHIEVEMENT_TYPE_UNSPECIFIED` (value: `"ACHIEVEMENT_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `INCREMENTAL` (value: `"INCREMENTAL"`)





## Enum: InitialStateEnum


* `INITIAL_STATE_UNSPECIFIED` (value: `"INITIAL_STATE_UNSPECIFIED"`)

* `HIDDEN` (value: `"HIDDEN"`)

* `REVEALED` (value: `"REVEALED"`)




