# GooglePlayGameServices.PlayerAchievement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achievementState** | **String** | The state of the achievement. | [optional] 
**currentSteps** | **Number** | The current steps for an incremental achievement. | [optional] 
**experiencePoints** | **String** | Experience points earned for the achievement. This field is absent for achievements that have not yet been unlocked and 0 for achievements that have been unlocked by testers but that are unpublished. | [optional] 
**formattedCurrentStepsString** | **String** | The current steps for an incremental achievement as a string. | [optional] 
**id** | **String** | The ID of the achievement. | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#playerAchievement&#x60;. | [optional] 
**lastUpdatedTimestamp** | **String** | The timestamp of the last modification to this achievement&#39;s state. | [optional] 



## Enum: AchievementStateEnum


* `HIDDEN` (value: `"HIDDEN"`)

* `REVEALED` (value: `"REVEALED"`)

* `UNLOCKED` (value: `"UNLOCKED"`)




