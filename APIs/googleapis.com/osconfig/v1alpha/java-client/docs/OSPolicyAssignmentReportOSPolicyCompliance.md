

# OSPolicyAssignmentReportOSPolicyCompliance

Compliance data for an OS policy

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**complianceState** | [**ComplianceStateEnum**](#ComplianceStateEnum) | The compliance state of the OS policy. |  [optional] |
|**complianceStateReason** | **String** | The reason for the OS policy to be in an unknown compliance state. This field is always populated when &#x60;compliance_state&#x60; is &#x60;UNKNOWN&#x60;. If populated, the field can contain one of the following values: * &#x60;vm-not-running&#x60;: The VM was not running. * &#x60;os-policies-not-supported-by-agent&#x60;: The version of the OS Config agent running on the VM does not support running OS policies. * &#x60;no-agent-detected&#x60;: The OS Config agent is not detected for the VM. * &#x60;resource-execution-errors&#x60;: The OS Config agent encountered errors while executing one or more resources in the policy. See &#x60;os_policy_resource_compliances&#x60; for details. * &#x60;task-timeout&#x60;: The task sent to the agent to apply the policy timed out. * &#x60;unexpected-agent-state&#x60;: The OS Config agent did not report the final status of the task that attempted to apply the policy. Instead, the agent unexpectedly started working on a different task. This mostly happens when the agent or VM unexpectedly restarts while applying OS policies. * &#x60;internal-service-errors&#x60;: Internal service errors were encountered while attempting to apply the policy. |  [optional] |
|**osPolicyId** | **String** | The OS policy id |  [optional] |
|**osPolicyResourceCompliances** | [**List&lt;OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceCompliance&gt;**](OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceCompliance.md) | Compliance data for each resource within the policy that is applied to the VM. |  [optional] |



## Enum: ComplianceStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| COMPLIANT | &quot;COMPLIANT&quot; |
| NON_COMPLIANT | &quot;NON_COMPLIANT&quot; |



