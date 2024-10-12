# OsConfigApi.InstanceOSPoliciesComplianceOSPolicyCompliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**osPolicyAssignment** | **String** | Reference to the &#x60;OSPolicyAssignment&#x60; API resource that the &#x60;OSPolicy&#x60; belongs to. Format: &#x60;projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}&#x60; | [optional] 
**osPolicyId** | **String** | The OS policy id | [optional] 
**osPolicyResourceCompliances** | [**[OSPolicyResourceCompliance]**](OSPolicyResourceCompliance.md) | Compliance data for each &#x60;OSPolicyResource&#x60; that is applied to the VM. | [optional] 
**state** | **String** | Compliance state of the OS policy. | [optional] 



## Enum: StateEnum


* `OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED` (value: `"OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED"`)

* `COMPLIANT` (value: `"COMPLIANT"`)

* `NON_COMPLIANT` (value: `"NON_COMPLIANT"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `NO_OS_POLICIES_APPLICABLE` (value: `"NO_OS_POLICIES_APPLICABLE"`)




