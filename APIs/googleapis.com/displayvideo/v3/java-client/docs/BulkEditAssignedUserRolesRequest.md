

# BulkEditAssignedUserRolesRequest

Request message for BulkEditAssignedUserRoles.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAssignedUserRoles** | [**List&lt;AssignedUserRole&gt;**](AssignedUserRole.md) | The assigned user roles to create in batch, specified as a list of AssignedUserRoles. |  [optional] |
|**deletedAssignedUserRoles** | **List&lt;String&gt;** | The assigned user roles to delete in batch, specified as a list of assigned_user_role_ids. The format of assigned_user_role_id is &#x60;entityType-entityid&#x60;, for example &#x60;partner-123&#x60;. |  [optional] |



