

# CleanupPolicy

Artifact policy configuration for repository cleanup policies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Policy action. |  [optional] |
|**condition** | [**CleanupPolicyCondition**](CleanupPolicyCondition.md) |  |  [optional] |
|**id** | **String** | The user-provided ID of the cleanup policy. |  [optional] |
|**mostRecentVersions** | [**CleanupPolicyMostRecentVersions**](CleanupPolicyMostRecentVersions.md) |  |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACTION_UNSPECIFIED | &quot;ACTION_UNSPECIFIED&quot; |
| DELETE | &quot;DELETE&quot; |
| KEEP | &quot;KEEP&quot; |



