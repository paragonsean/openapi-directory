

# LinkAADtoUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadTenantIds** | **List&lt;UUID&gt;** | An array of AAD tenant data needed to link the user to the tenants |  |
|**role** | [**RoleEnum**](#RoleEnum) | The role of the user to be added |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN | &quot;admin&quot; |
| COLLABORATOR | &quot;collaborator&quot; |
| MEMBER | &quot;member&quot; |



