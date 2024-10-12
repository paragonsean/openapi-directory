

# OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceCompliance

Compliance data for an OS policy resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**complianceState** | [**ComplianceStateEnum**](#ComplianceStateEnum) | The compliance state of the resource. |  [optional] |
|**complianceStateReason** | **String** | A reason for the resource to be in the given compliance state. This field is always populated when &#x60;compliance_state&#x60; is &#x60;UNKNOWN&#x60;. The following values are supported when &#x60;compliance_state &#x3D;&#x3D; UNKNOWN&#x60; * &#x60;execution-errors&#x60;: Errors were encountered by the agent while executing the resource and the compliance state couldn&#39;t be determined. * &#x60;execution-skipped-by-agent&#x60;: Resource execution was skipped by the agent because errors were encountered while executing prior resources in the OS policy. * &#x60;os-policy-execution-attempt-failed&#x60;: The execution of the OS policy containing this resource failed and the compliance state couldn&#39;t be determined. |  [optional] |
|**configSteps** | [**List&lt;OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStep&gt;**](OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStep.md) | Ordered list of configuration completed by the agent for the OS policy resource. |  [optional] |
|**execResourceOutput** | [**OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutput**](OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceExecResourceOutput.md) |  |  [optional] |
|**osPolicyResourceId** | **String** | The ID of the OS policy resource. |  [optional] |



## Enum: ComplianceStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| COMPLIANT | &quot;COMPLIANT&quot; |
| NON_COMPLIANT | &quot;NON_COMPLIANT&quot; |



