

# OSPolicyAssignment

OS policy assignment is an API resource that is used to apply a set of OS policies to a dynamically targeted group of Compute Engine VM instances. An OS policy is used to define the desired state configuration for a Compute Engine VM instance through a set of configuration resources that provide capabilities such as installing or removing software packages, or executing a script. For more information, see [OS policy and OS policy assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseline** | **Boolean** | Output only. Indicates that this revision has been successfully rolled out in this zone and new VMs will be assigned OS policies from this revision. For a given OS policy assignment, there is only one revision with a value of &#x60;true&#x60; for this field. |  [optional] [readonly] |
|**deleted** | **Boolean** | Output only. Indicates that this revision deletes the OS policy assignment. |  [optional] [readonly] |
|**description** | **String** | OS policy assignment description. Length of the description is limited to 1024 characters. |  [optional] |
|**etag** | **String** | The etag for this OS policy assignment. If this is provided on update, it must match the server&#39;s etag. |  [optional] |
|**instanceFilter** | [**OSPolicyAssignmentInstanceFilter**](OSPolicyAssignmentInstanceFilter.md) |  |  [optional] |
|**name** | **String** | Resource name. Format: &#x60;projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id}&#x60; This field is ignored when you create an OS policy assignment. |  [optional] |
|**osPolicies** | [**List&lt;OSPolicy&gt;**](OSPolicy.md) | Required. List of OS policies to be applied to the VMs. |  [optional] |
|**reconciling** | **Boolean** | Output only. Indicates that reconciliation is in progress for the revision. This value is &#x60;true&#x60; when the &#x60;rollout_state&#x60; is one of: * IN_PROGRESS * CANCELLING |  [optional] [readonly] |
|**revisionCreateTime** | **String** | Output only. The timestamp that the revision was created. |  [optional] [readonly] |
|**revisionId** | **String** | Output only. The assignment revision ID A new revision is committed whenever a rollout is triggered for a OS policy assignment |  [optional] [readonly] |
|**rollout** | [**OSPolicyAssignmentRollout**](OSPolicyAssignmentRollout.md) |  |  [optional] |
|**rolloutState** | [**RolloutStateEnum**](#RolloutStateEnum) | Output only. OS policy assignment rollout state |  [optional] [readonly] |
|**uid** | **String** | Output only. Server generated unique id for the OS policy assignment resource. |  [optional] [readonly] |



## Enum: RolloutStateEnum

| Name | Value |
|---- | -----|
| ROLLOUT_STATE_UNSPECIFIED | &quot;ROLLOUT_STATE_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |



