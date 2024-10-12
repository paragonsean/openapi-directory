# GooglePlayGameServices.AchievementUpdateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievementId** | **String** | The achievement this update is was applied to. | [optional] 
**currentState** | **String** | The current state of the achievement. | [optional] 
**currentSteps** | **Number** | The current steps recorded for this achievement if it is incremental. | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#achievementUpdateResponse&#x60;. | [optional] 
**newlyUnlocked** | **Boolean** | Whether this achievement was newly unlocked (that is, whether the unlock request for the achievement was the first for the player). | [optional] 
**updateOccurred** | **Boolean** | Whether the requested updates actually affected the achievement. | [optional] 



## Enum: CurrentStateEnum


* `HIDDEN` (value: `"HIDDEN"`)

* `REVEALED` (value: `"REVEALED"`)

* `UNLOCKED` (value: `"UNLOCKED"`)




