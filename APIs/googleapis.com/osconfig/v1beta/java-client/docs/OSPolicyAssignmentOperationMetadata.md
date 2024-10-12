

# OSPolicyAssignmentOperationMetadata

OS policy assignment operation metadata provided by OS policy assignment API methods that return long running operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiMethod** | [**ApiMethodEnum**](#ApiMethodEnum) | The OS policy assignment API method. |  [optional] |
|**osPolicyAssignment** | **String** | Reference to the &#x60;OSPolicyAssignment&#x60; API resource. Format: &#x60;projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}&#x60; |  [optional] |
|**rolloutStartTime** | **String** | Rollout start time |  [optional] |
|**rolloutState** | [**RolloutStateEnum**](#RolloutStateEnum) | State of the rollout |  [optional] |
|**rolloutUpdateTime** | **String** | Rollout update time |  [optional] |



## Enum: ApiMethodEnum

| Name | Value |
|---- | -----|
| API_METHOD_UNSPECIFIED | &quot;API_METHOD_UNSPECIFIED&quot; |
| CREATE | &quot;CREATE&quot; |
| UPDATE | &quot;UPDATE&quot; |
| DELETE | &quot;DELETE&quot; |



## Enum: RolloutStateEnum

| Name | Value |
|---- | -----|
| ROLLOUT_STATE_UNSPECIFIED | &quot;ROLLOUT_STATE_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |



