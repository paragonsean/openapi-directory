

# GoogleCloudPolicysimulatorV1alphaExplainedPolicy

Details about how a specific IAM Policy contributed to the access check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Indicates whether _this policy_ provides the specified permission to the specified principal for the specified resource. This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another policy that overrides this policy. To determine whether the principal actually has the permission, use the &#x60;access&#x60; field in the TroubleshootIamPolicyResponse. |  [optional] |
|**bindingExplanations** | [**List&lt;GoogleCloudPolicysimulatorV1alphaBindingExplanation&gt;**](GoogleCloudPolicysimulatorV1alphaBindingExplanation.md) | Details about how each binding in the policy affects the principal&#39;s ability, or inability, to use the permission for the resource. If the user who created the Replay does not have access to the policy, this field is omitted. |  [optional] |
|**fullResourceName** | **String** | The full resource name that identifies the resource. For example, &#x60;//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance&#x60;. If the user who created the Replay does not have access to the policy, this field is omitted. For examples of full resource names for Google Cloud services, see https://cloud.google.com/iam/help/troubleshooter/full-resource-names. |  [optional] |
|**policy** | [**GoogleIamV1Policy**](GoogleIamV1Policy.md) |  |  [optional] |
|**relevance** | [**RelevanceEnum**](#RelevanceEnum) | The relevance of this policy to the overall determination in the TroubleshootIamPolicyResponse. If the user who created the Replay does not have access to the policy, this field is omitted. |  [optional] |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| ACCESS_STATE_UNSPECIFIED | &quot;ACCESS_STATE_UNSPECIFIED&quot; |
| GRANTED | &quot;GRANTED&quot; |
| NOT_GRANTED | &quot;NOT_GRANTED&quot; |
| UNKNOWN_CONDITIONAL | &quot;UNKNOWN_CONDITIONAL&quot; |
| UNKNOWN_INFO_DENIED | &quot;UNKNOWN_INFO_DENIED&quot; |



## Enum: RelevanceEnum

| Name | Value |
|---- | -----|
| HEURISTIC_RELEVANCE_UNSPECIFIED | &quot;HEURISTIC_RELEVANCE_UNSPECIFIED&quot; |
| NORMAL | &quot;NORMAL&quot; |
| HIGH | &quot;HIGH&quot; |



