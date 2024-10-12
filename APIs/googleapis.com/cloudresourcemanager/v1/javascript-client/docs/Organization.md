# CloudResourceManagerApi.Organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **String** | Timestamp when the Organization was created. Assigned by the server. | [optional] 
**displayName** | **String** | A human-readable string that refers to the Organization in the Google Cloud console. This string is set by the server and cannot be changed. The string will be set to the primary domain (for example, \&quot;google.com\&quot;) of the G Suite customer that owns the organization. | [optional] 
**lifecycleState** | **String** | The organization&#39;s current lifecycle state. Assigned by the server. | [optional] 
**name** | **String** | Output only. The resource name of the organization. This is the organization&#39;s relative path in the API. Its format is \&quot;organizations/[organization_id]\&quot;. For example, \&quot;organizations/1234\&quot;. | [optional] 
**owner** | [**OrganizationOwner**](OrganizationOwner.md) |  | [optional] 



## Enum: LifecycleStateEnum


* `LIFECYCLE_STATE_UNSPECIFIED` (value: `"LIFECYCLE_STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETE_REQUESTED` (value: `"DELETE_REQUESTED"`)




