

# UserCreateParameters

Parameters supplied to the Create User operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Email address. Must not be empty and must be unique within the service instance. |  |
|**firstName** | **String** | First name. |  |
|**lastName** | **String** | Last name. |  |
|**note** | **String** | Optional note about a user set by the administrator. |  [optional] |
|**password** | **String** | User Password. |  |
|**state** | [**StateEnum**](#StateEnum) | Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| BLOCKED | &quot;Blocked&quot; |



