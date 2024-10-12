# FitbitPlusApi.RewardProgramResourceAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgetUnit** | **String** | Unit of the budget for the reard program. | [optional] [default to &#39;dollar&#39;]
**budgetValue** | **Number** | Value of the budget for the reward program. (Must be greater than 0) | 
**description** | **String** | Description of the reward program - designed to be a comprehensive text description | [optional] 
**durationActive** | **Number** | Number of days that a program can be active after it has been activated for a patient. (Must be greater than 0) | [optional] [default to 540]
**endAt** | **String** | Date at which the reward program ends. (Must be after the start_at) | 
**frozen** | **Boolean** | If true, the reward program cannot be activated for a patient and new rewards cannot be created for the program. | [optional] [default to false]
**fulfillAsEarned** | **Boolean** | If true, the rewards created for a patient for the program can be fulfulled as they are earned. If false, the rewards should only be fulfilled when the program is deactivated. | [optional] [default to false]
**name** | **String** | Name of the reward program | 
**startAt** | **String** | Date at which the reward program starts. | 
**tagline** | **String** | Tagline of the reward program - designed to be one line | [optional] 



## Enum: BudgetUnitEnum


* `dollar` (value: `"dollar"`)

* `point` (value: `"point"`)

* `credit` (value: `"credit"`)




