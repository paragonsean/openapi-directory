# PolicyTroubleshooterApi.GoogleCloudPolicytroubleshooterV1betaBindingExplanation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | Indicates whether _this binding_ provides the specified permission to the specified member for the specified resource. This field does _not_ indicate whether the member actually has the permission for the resource. There might be another binding that overrides this binding. To determine whether the member actually has the permission, use the &#x60;access&#x60; field in the TroubleshootIamPolicyResponse. | [optional] 
**condition** | [**GoogleTypeExpr**](GoogleTypeExpr.md) |  | [optional] 
**memberships** | [**{String: GoogleCloudPolicytroubleshooterV1betaBindingExplanationAnnotatedMembership}**](GoogleCloudPolicytroubleshooterV1betaBindingExplanationAnnotatedMembership.md) | Indicates whether each member in the binding includes the member specified in the request, either directly or indirectly. Each key identifies a member in the binding, and each value indicates whether the member in the binding includes the member in the request. For example, suppose that a binding includes the following members: * &#x60;user:alice@example.com&#x60; * &#x60;group:product-eng@example.com&#x60; You want to troubleshoot access for &#x60;user:bob@example.com&#x60;. This user is a member of the group &#x60;group:product-eng@example.com&#x60;. For the first member in the binding, the key is &#x60;user:alice@example.com&#x60;, and the &#x60;membership&#x60; field in the value is set to &#x60;MEMBERSHIP_NOT_INCLUDED&#x60;. For the second member in the binding, the key is &#x60;group:product-eng@example.com&#x60;, and the &#x60;membership&#x60; field in the value is set to &#x60;MEMBERSHIP_INCLUDED&#x60;. | [optional] 
**relevance** | **String** | The relevance of this binding to the overall determination for the entire policy. | [optional] 
**role** | **String** | The role that this binding grants. For example, &#x60;roles/compute.serviceAgent&#x60;. For a complete list of predefined IAM roles, as well as the permissions in each role, see https://cloud.google.com/iam/help/roles/reference. | [optional] 
**rolePermission** | **String** | Indicates whether the role granted by this binding contains the specified permission. | [optional] 
**rolePermissionRelevance** | **String** | The relevance of the permission&#39;s existence, or nonexistence, in the role to the overall determination for the entire policy. | [optional] 



## Enum: AccessEnum


* `ACCESS_STATE_UNSPECIFIED` (value: `"ACCESS_STATE_UNSPECIFIED"`)

* `GRANTED` (value: `"GRANTED"`)

* `NOT_GRANTED` (value: `"NOT_GRANTED"`)

* `UNKNOWN_CONDITIONAL` (value: `"UNKNOWN_CONDITIONAL"`)

* `UNKNOWN_INFO_DENIED` (value: `"UNKNOWN_INFO_DENIED"`)





## Enum: RelevanceEnum


* `HEURISTIC_RELEVANCE_UNSPECIFIED` (value: `"HEURISTIC_RELEVANCE_UNSPECIFIED"`)

* `NORMAL` (value: `"NORMAL"`)

* `HIGH` (value: `"HIGH"`)





## Enum: RolePermissionEnum


* `UNSPECIFIED` (value: `"ROLE_PERMISSION_UNSPECIFIED"`)

* `INCLUDED` (value: `"ROLE_PERMISSION_INCLUDED"`)

* `NOT_INCLUDED` (value: `"ROLE_PERMISSION_NOT_INCLUDED"`)

* `UNKNOWN_INFO_DENIED` (value: `"ROLE_PERMISSION_UNKNOWN_INFO_DENIED"`)





## Enum: RolePermissionRelevanceEnum


* `HEURISTIC_RELEVANCE_UNSPECIFIED` (value: `"HEURISTIC_RELEVANCE_UNSPECIFIED"`)

* `NORMAL` (value: `"NORMAL"`)

* `HIGH` (value: `"HIGH"`)




