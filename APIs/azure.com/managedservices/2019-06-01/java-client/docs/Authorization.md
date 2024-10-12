

# Authorization

Authorization tuple containing principal Id (of user/service principal/security group) and role definition id.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | Principal Id of the security group/service principal/user that would be assigned permissions to the projected subscription |  |
|**roleDefinitionId** | **String** | The role definition identifier. This role will define all the permissions that the security group/service principal/user must have on the projected subscription. This role cannot be an owner role. |  |



