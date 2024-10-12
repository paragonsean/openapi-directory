

# ShareInvitationSummary

A share invitation summary return object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**shareInvitationId** | [**String**](String.md) |  |  [optional] |
|**sharedBy** | **String** | An Amazon Web Services account ID. |  [optional] |
|**sharedWith** | **String** | The Amazon Web Services account ID, IAM role, organization ID, or organizational unit (OU) ID with which the workload, lens, or profile is shared. |  [optional] |
|**permissionType** | **PermissionType** |  |  [optional] |
|**shareResourceType** | [**ShareResourceType**](ShareResourceType.md) |  |  [optional] |
|**workloadName** | **String** | &lt;p&gt;The name of the workload.&lt;/p&gt; &lt;p&gt;The name must be unique within an account within an Amazon Web Services Region. Spaces and capitalization are ignored when checking for uniqueness.&lt;/p&gt; |  [optional] |
|**workloadId** | **String** | The ID assigned to the workload. This ID is unique within an Amazon Web Services Region. |  [optional] |
|**lensName** | **String** | The full name of the lens. |  [optional] |
|**lensArn** | [**String**](String.md) |  |  [optional] |
|**profileName** | [**String**](String.md) |  |  [optional] |
|**profileArn** | [**String**](String.md) |  |  [optional] |



