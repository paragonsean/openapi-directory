

# GoogleCloudPolicytroubleshooterV1BindingExplanation

Details about how a binding in a policy affects a principal's ability to use a permission.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Required. Indicates whether _this binding_ provides the specified permission to the specified principal for the specified resource. This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another binding that overrides this binding. To determine whether the principal actually has the permission, use the &#x60;access&#x60; field in the TroubleshootIamPolicyResponse. |  [optional] |
|**condition** | [**GoogleTypeExpr**](GoogleTypeExpr.md) |  |  [optional] |
|**memberships** | [**Map&lt;String, GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembership&gt;**](GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembership.md) | Indicates whether each principal in the binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the binding, and each value indicates whether the principal in the binding includes the principal in the request. For example, suppose that a binding includes the following principals: * &#x60;user:alice@example.com&#x60; * &#x60;group:product-eng@example.com&#x60; You want to troubleshoot access for &#x60;user:bob@example.com&#x60;. This user is a principal of the group &#x60;group:product-eng@example.com&#x60;. For the first principal in the binding, the key is &#x60;user:alice@example.com&#x60;, and the &#x60;membership&#x60; field in the value is set to &#x60;MEMBERSHIP_NOT_INCLUDED&#x60;. For the second principal in the binding, the key is &#x60;group:product-eng@example.com&#x60;, and the &#x60;membership&#x60; field in the value is set to &#x60;MEMBERSHIP_INCLUDED&#x60;. |  [optional] |
|**relevance** | [**RelevanceEnum**](#RelevanceEnum) | The relevance of this binding to the overall determination for the entire policy. |  [optional] |
|**role** | **String** | The role that this binding grants. For example, &#x60;roles/compute.serviceAgent&#x60;. For a complete list of predefined IAM roles, as well as the permissions in each role, see https://cloud.google.com/iam/help/roles/reference. |  [optional] |
|**rolePermission** | [**RolePermissionEnum**](#RolePermissionEnum) | Indicates whether the role granted by this binding contains the specified permission. |  [optional] |
|**rolePermissionRelevance** | [**RolePermissionRelevanceEnum**](#RolePermissionRelevanceEnum) | The relevance of the permission&#39;s existence, or nonexistence, in the role to the overall determination for the entire policy. |  [optional] |



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



## Enum: RolePermissionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ROLE_PERMISSION_UNSPECIFIED&quot; |
| INCLUDED | &quot;ROLE_PERMISSION_INCLUDED&quot; |
| NOT_INCLUDED | &quot;ROLE_PERMISSION_NOT_INCLUDED&quot; |
| UNKNOWN_INFO_DENIED | &quot;ROLE_PERMISSION_UNKNOWN_INFO_DENIED&quot; |



## Enum: RolePermissionRelevanceEnum

| Name | Value |
|---- | -----|
| HEURISTIC_RELEVANCE_UNSPECIFIED | &quot;HEURISTIC_RELEVANCE_UNSPECIFIED&quot; |
| NORMAL | &quot;NORMAL&quot; |
| HIGH | &quot;HIGH&quot; |



