

# OSPolicyAssignmentReportOSPolicyComplianceOSPolicyResourceComplianceOSPolicyResourceConfigStep

Step performed by the OS Config agent for configuring an `OSPolicy` resource to its desired state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | An error message recorded during the execution of this step. Only populated if errors were encountered during this step execution. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Configuration step type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| VALIDATION | &quot;VALIDATION&quot; |
| DESIRED_STATE_CHECK | &quot;DESIRED_STATE_CHECK&quot; |
| DESIRED_STATE_ENFORCEMENT | &quot;DESIRED_STATE_ENFORCEMENT&quot; |
| DESIRED_STATE_CHECK_POST_ENFORCEMENT | &quot;DESIRED_STATE_CHECK_POST_ENFORCEMENT&quot; |



