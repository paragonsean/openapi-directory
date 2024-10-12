

# OSPolicyResourceCompliance

Compliance data for an OS policy resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configSteps** | [**List&lt;OSPolicyResourceConfigStep&gt;**](OSPolicyResourceConfigStep.md) | Ordered list of configuration steps taken by the agent for the OS policy resource. |  [optional] |
|**execResourceOutput** | [**OSPolicyResourceComplianceExecResourceOutput**](OSPolicyResourceComplianceExecResourceOutput.md) |  |  [optional] |
|**osPolicyResourceId** | **String** | The id of the OS policy resource. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Compliance state of the OS policy resource. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED | &quot;OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED&quot; |
| COMPLIANT | &quot;COMPLIANT&quot; |
| NON_COMPLIANT | &quot;NON_COMPLIANT&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| NO_OS_POLICIES_APPLICABLE | &quot;NO_OS_POLICIES_APPLICABLE&quot; |



