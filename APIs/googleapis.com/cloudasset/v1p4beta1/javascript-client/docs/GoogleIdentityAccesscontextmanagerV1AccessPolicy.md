# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1AccessPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | Output only. An opaque identifier for the current version of the &#x60;AccessPolicy&#x60;. This will always be a strongly validated etag, meaning that two Access Polices will be identical if and only if their etags are identical. Clients should not expect this to be in any specific format. | [optional] 
**name** | **String** | Output only. Resource name of the &#x60;AccessPolicy&#x60;. Format: &#x60;accessPolicies/{access_policy}&#x60; | [optional] 
**parent** | **String** | Required. The parent of this &#x60;AccessPolicy&#x60; in the Cloud Resource Hierarchy. Currently immutable once created. Format: &#x60;organizations/{organization_id}&#x60; | [optional] 
**scopes** | **[String]** | The scopes of a policy define which resources an ACM policy can restrict, and where ACM resources can be referenced. For example, a policy with scopes&#x3D;[\&quot;folders/123\&quot;] has the following behavior: - vpcsc perimeters can only restrict projects within folders/123 - access levels can only be referenced by resources within folders/123. If empty, there are no limitations on which resources can be restricted by an ACM policy, and there are no limitations on where ACM resources can be referenced. Only one policy can include a given scope (attempting to create a second policy which includes \&quot;folders/123\&quot; will result in an error). Currently, scopes cannot be modified after a policy is created. Currently, policies can only have a single scope. Format: list of &#x60;folders/{folder_number}&#x60; or &#x60;projects/{project_number}&#x60; | [optional] 
**title** | **String** | Required. Human readable title. Does not affect behavior. | [optional] 


