

# AppRoleAssignment

AppRoleAssignment information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The role id that was assigned to the principal. This role must be declared by the target resource application resourceId in its appRoles property. |  [optional] |
|**principalDisplayName** | **String** | The display name of the principal that was granted the access. |  [optional] |
|**principalId** | **String** | The unique identifier (objectId) for the principal being granted the access. |  [optional] |
|**principalType** | **String** | The type of principal. This can either be \&quot;User\&quot;, \&quot;Group\&quot; or \&quot;ServicePrincipal\&quot;. |  [optional] |
|**resourceDisplayName** | **String** | The display name of the resource to which the assignment was made. |  [optional] |
|**resourceId** | **String** | The unique identifier (objectId) for the target resource (service principal) for which the assignment was made. |  [optional] |



