# GooglePlayGameServices.AchievementUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievementId** | **String** | The achievement this update is being applied to. | [optional] 
**incrementPayload** | [**GamesAchievementIncrement**](GamesAchievementIncrement.md) |  | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#achievementUpdateRequest&#x60;. | [optional] 
**setStepsAtLeastPayload** | [**GamesAchievementSetStepsAtLeast**](GamesAchievementSetStepsAtLeast.md) |  | [optional] 
**updateType** | **String** | The type of update being applied. | [optional] 



## Enum: UpdateTypeEnum


* `REVEAL` (value: `"REVEAL"`)

* `UNLOCK` (value: `"UNLOCK"`)

* `INCREMENT` (value: `"INCREMENT"`)

* `SET_STEPS_AT_LEAST` (value: `"SET_STEPS_AT_LEAST"`)




