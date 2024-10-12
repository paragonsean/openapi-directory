# BatchApi.LifecyclePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Action to execute when ActionCondition is true. When RETRY_TASK is specified, we will retry failed tasks if we notice any exit code match and fail tasks if no match is found. Likewise, when FAIL_TASK is specified, we will fail tasks if we notice any exit code match and retry tasks if no match is found. | [optional] 
**actionCondition** | [**ActionCondition**](ActionCondition.md) |  | [optional] 



## Enum: ActionEnum


* `ACTION_UNSPECIFIED` (value: `"ACTION_UNSPECIFIED"`)

* `RETRY_TASK` (value: `"RETRY_TASK"`)

* `FAIL_TASK` (value: `"FAIL_TASK"`)




