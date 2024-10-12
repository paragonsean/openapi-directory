

# GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponse

Response for TroubleshootIamPolicy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Indicates whether the principal has the specified permission for the specified resource, based on evaluating all of the applicable IAM policies. |  [optional] |
|**errors** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | The general errors contained in the troubleshooting response. |  [optional] |
|**explainedPolicies** | [**List&lt;GoogleCloudPolicytroubleshooterV1ExplainedPolicy&gt;**](GoogleCloudPolicytroubleshooterV1ExplainedPolicy.md) | List of IAM policies that were evaluated to check the principal&#39;s permissions, with annotations to indicate how each policy contributed to the final result. The list of policies can include the policy for the resource itself. It can also include policies that are inherited from higher levels of the resource hierarchy, including the organization, the folder, and the project. To learn more about the resource hierarchy, see https://cloud.google.com/iam/help/resource-hierarchy. |  [optional] |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| ACCESS_STATE_UNSPECIFIED | &quot;ACCESS_STATE_UNSPECIFIED&quot; |
| GRANTED | &quot;GRANTED&quot; |
| NOT_GRANTED | &quot;NOT_GRANTED&quot; |
| UNKNOWN_CONDITIONAL | &quot;UNKNOWN_CONDITIONAL&quot; |
| UNKNOWN_INFO_DENIED | &quot;UNKNOWN_INFO_DENIED&quot; |



