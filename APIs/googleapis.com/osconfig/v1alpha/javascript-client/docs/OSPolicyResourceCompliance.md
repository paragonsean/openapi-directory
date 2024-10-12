# OsConfigApi.OSPolicyResourceCompliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configSteps** | [**[OSPolicyResourceConfigStep]**](OSPolicyResourceConfigStep.md) | Ordered list of configuration steps taken by the agent for the OS policy resource. | [optional] 
**execResourceOutput** | [**OSPolicyResourceComplianceExecResourceOutput**](OSPolicyResourceComplianceExecResourceOutput.md) |  | [optional] 
**osPolicyResourceId** | **String** | The id of the OS policy resource. | [optional] 
**state** | **String** | Compliance state of the OS policy resource. | [optional] 



## Enum: StateEnum


* `OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED` (value: `"OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED"`)

* `COMPLIANT` (value: `"COMPLIANT"`)

* `NON_COMPLIANT` (value: `"NON_COMPLIANT"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `NO_OS_POLICIES_APPLICABLE` (value: `"NO_OS_POLICIES_APPLICABLE"`)




