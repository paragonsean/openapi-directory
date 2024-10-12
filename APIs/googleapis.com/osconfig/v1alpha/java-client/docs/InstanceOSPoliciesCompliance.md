

# InstanceOSPoliciesCompliance

This API resource represents the OS policies compliance data for a Compute Engine virtual machine (VM) instance at a given point in time. A Compute Engine VM can have multiple OS policy assignments, and each assignment can have multiple OS policies. As a result, multiple OS policies could be applied to a single VM. You can use this API resource to determine both the compliance state of your VM as well as the compliance state of an individual OS policy. For more information, see [View compliance](https://cloud.google.com/compute/docs/os-configuration-management/view-compliance).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detailedState** | **String** | Output only. Detailed compliance state of the VM. This field is populated only when compliance state is &#x60;UNKNOWN&#x60;. It may contain one of the following values: * &#x60;no-compliance-data&#x60;: Compliance data is not available for this VM. * &#x60;no-agent-detected&#x60;: OS Config agent is not detected for this VM. * &#x60;config-not-supported-by-agent&#x60;: The version of the OS Config agent running on this VM does not support configuration management. * &#x60;inactive&#x60;: VM is not running. * &#x60;internal-service-errors&#x60;: There were internal service errors encountered while enforcing compliance. * &#x60;agent-errors&#x60;: OS config agent encountered errors while enforcing compliance. |  [optional] [readonly] |
|**detailedStateReason** | **String** | Output only. The reason for the &#x60;detailed_state&#x60; of the VM (if any). |  [optional] [readonly] |
|**instance** | **String** | Output only. The Compute Engine VM instance name. |  [optional] [readonly] |
|**lastComplianceCheckTime** | **String** | Output only. Timestamp of the last compliance check for the VM. |  [optional] [readonly] |
|**lastComplianceRunId** | **String** | Output only. Unique identifier for the last compliance run. This id will be logged by the OS config agent during a compliance run and can be used for debugging and tracing purpose. |  [optional] [readonly] |
|**name** | **String** | Output only. The &#x60;InstanceOSPoliciesCompliance&#x60; API resource name. Format: &#x60;projects/{project_number}/locations/{location}/instanceOSPoliciesCompliances/{instance_id}&#x60; |  [optional] [readonly] |
|**osPolicyCompliances** | [**List&lt;InstanceOSPoliciesComplianceOSPolicyCompliance&gt;**](InstanceOSPoliciesComplianceOSPolicyCompliance.md) | Output only. Compliance data for each &#x60;OSPolicy&#x60; that is applied to the VM. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Compliance state of the VM. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED | &quot;OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED&quot; |
| COMPLIANT | &quot;COMPLIANT&quot; |
| NON_COMPLIANT | &quot;NON_COMPLIANT&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| NO_OS_POLICIES_APPLICABLE | &quot;NO_OS_POLICIES_APPLICABLE&quot; |



