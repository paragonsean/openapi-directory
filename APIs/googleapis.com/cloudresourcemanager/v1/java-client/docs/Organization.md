

# Organization

The root node in the resource hierarchy to which a particular entity's (e.g., company) resources belong.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **String** | Timestamp when the Organization was created. Assigned by the server. |  [optional] |
|**displayName** | **String** | A human-readable string that refers to the Organization in the Google Cloud console. This string is set by the server and cannot be changed. The string will be set to the primary domain (for example, \&quot;google.com\&quot;) of the G Suite customer that owns the organization. |  [optional] |
|**lifecycleState** | [**LifecycleStateEnum**](#LifecycleStateEnum) | The organization&#39;s current lifecycle state. Assigned by the server. |  [optional] |
|**name** | **String** | Output only. The resource name of the organization. This is the organization&#39;s relative path in the API. Its format is \&quot;organizations/[organization_id]\&quot;. For example, \&quot;organizations/1234\&quot;. |  [optional] |
|**owner** | [**OrganizationOwner**](OrganizationOwner.md) |  |  [optional] |



## Enum: LifecycleStateEnum

| Name | Value |
|---- | -----|
| LIFECYCLE_STATE_UNSPECIFIED | &quot;LIFECYCLE_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETE_REQUESTED | &quot;DELETE_REQUESTED&quot; |



