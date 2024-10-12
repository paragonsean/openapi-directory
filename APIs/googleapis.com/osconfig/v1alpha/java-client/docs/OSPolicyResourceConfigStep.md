

# OSPolicyResourceConfigStep

Step performed by the OS Config agent for configuring an `OSPolicyResource` to its desired state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | An error message recorded during the execution of this step. Only populated when outcome is FAILED. |  [optional] |
|**outcome** | [**OutcomeEnum**](#OutcomeEnum) | Outcome of the configuration step. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Configuration step type. |  [optional] |



## Enum: OutcomeEnum

| Name | Value |
|---- | -----|
| OUTCOME_UNSPECIFIED | &quot;OUTCOME_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| VALIDATION | &quot;VALIDATION&quot; |
| DESIRED_STATE_CHECK | &quot;DESIRED_STATE_CHECK&quot; |
| DESIRED_STATE_ENFORCEMENT | &quot;DESIRED_STATE_ENFORCEMENT&quot; |
| DESIRED_STATE_CHECK_POST_ENFORCEMENT | &quot;DESIRED_STATE_CHECK_POST_ENFORCEMENT&quot; |



