# OsConfigApi.GoogleCloudOsconfigV1OSPolicyAssignmentOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiMethod** | **String** | The OS policy assignment API method. | [optional] 
**osPolicyAssignment** | **String** | Reference to the &#x60;OSPolicyAssignment&#x60; API resource. Format: &#x60;projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}&#x60; | [optional] 
**rolloutStartTime** | **String** | Rollout start time | [optional] 
**rolloutState** | **String** | State of the rollout | [optional] 
**rolloutUpdateTime** | **String** | Rollout update time | [optional] 



## Enum: ApiMethodEnum


* `API_METHOD_UNSPECIFIED` (value: `"API_METHOD_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `UPDATE` (value: `"UPDATE"`)

* `DELETE` (value: `"DELETE"`)





## Enum: RolloutStateEnum


* `ROLLOUT_STATE_UNSPECIFIED` (value: `"ROLLOUT_STATE_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)




