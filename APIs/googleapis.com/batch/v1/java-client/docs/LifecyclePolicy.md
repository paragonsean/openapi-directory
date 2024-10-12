

# LifecyclePolicy

LifecyclePolicy describes how to deal with task failures based on different conditions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Action to execute when ActionCondition is true. When RETRY_TASK is specified, we will retry failed tasks if we notice any exit code match and fail tasks if no match is found. Likewise, when FAIL_TASK is specified, we will fail tasks if we notice any exit code match and retry tasks if no match is found. |  [optional] |
|**actionCondition** | [**ActionCondition**](ActionCondition.md) |  |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACTION_UNSPECIFIED | &quot;ACTION_UNSPECIFIED&quot; |
| RETRY_TASK | &quot;RETRY_TASK&quot; |
| FAIL_TASK | &quot;FAIL_TASK&quot; |



