# OsConfigApi.InstanceOSPoliciesCompliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailedState** | **String** | Output only. Detailed compliance state of the VM. This field is populated only when compliance state is &#x60;UNKNOWN&#x60;. It may contain one of the following values: * &#x60;no-compliance-data&#x60;: Compliance data is not available for this VM. * &#x60;no-agent-detected&#x60;: OS Config agent is not detected for this VM. * &#x60;config-not-supported-by-agent&#x60;: The version of the OS Config agent running on this VM does not support configuration management. * &#x60;inactive&#x60;: VM is not running. * &#x60;internal-service-errors&#x60;: There were internal service errors encountered while enforcing compliance. * &#x60;agent-errors&#x60;: OS config agent encountered errors while enforcing compliance. | [optional] [readonly] 
**detailedStateReason** | **String** | Output only. The reason for the &#x60;detailed_state&#x60; of the VM (if any). | [optional] [readonly] 
**instance** | **String** | Output only. The Compute Engine VM instance name. | [optional] [readonly] 
**lastComplianceCheckTime** | **String** | Output only. Timestamp of the last compliance check for the VM. | [optional] [readonly] 
**lastComplianceRunId** | **String** | Output only. Unique identifier for the last compliance run. This id will be logged by the OS config agent during a compliance run and can be used for debugging and tracing purpose. | [optional] [readonly] 
**name** | **String** | Output only. The &#x60;InstanceOSPoliciesCompliance&#x60; API resource name. Format: &#x60;projects/{project_number}/locations/{location}/instanceOSPoliciesCompliances/{instance_id}&#x60; | [optional] [readonly] 
**osPolicyCompliances** | [**[InstanceOSPoliciesComplianceOSPolicyCompliance]**](InstanceOSPoliciesComplianceOSPolicyCompliance.md) | Output only. Compliance data for each &#x60;OSPolicy&#x60; that is applied to the VM. | [optional] [readonly] 
**state** | **String** | Output only. Compliance state of the VM. | [optional] [readonly] 



## Enum: StateEnum


* `OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED` (value: `"OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED"`)

* `COMPLIANT` (value: `"COMPLIANT"`)

* `NON_COMPLIANT` (value: `"NON_COMPLIANT"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `NO_OS_POLICIES_APPLICABLE` (value: `"NO_OS_POLICIES_APPLICABLE"`)




