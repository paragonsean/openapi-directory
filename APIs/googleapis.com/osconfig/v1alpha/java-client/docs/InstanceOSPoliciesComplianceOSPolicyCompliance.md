

# InstanceOSPoliciesComplianceOSPolicyCompliance

Compliance data for an OS policy

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**osPolicyAssignment** | **String** | Reference to the &#x60;OSPolicyAssignment&#x60; API resource that the &#x60;OSPolicy&#x60; belongs to. Format: &#x60;projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}&#x60; |  [optional] |
|**osPolicyId** | **String** | The OS policy id |  [optional] |
|**osPolicyResourceCompliances** | [**List&lt;OSPolicyResourceCompliance&gt;**](OSPolicyResourceCompliance.md) | Compliance data for each &#x60;OSPolicyResource&#x60; that is applied to the VM. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Compliance state of the OS policy. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED | &quot;OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED&quot; |
| COMPLIANT | &quot;COMPLIANT&quot; |
| NON_COMPLIANT | &quot;NON_COMPLIANT&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| NO_OS_POLICIES_APPLICABLE | &quot;NO_OS_POLICIES_APPLICABLE&quot; |



