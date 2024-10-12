

# UserCreateParameterProperties

Parameters supplied to the Create User operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confirmation** | [**ConfirmationEnum**](#ConfirmationEnum) | Determines the type of confirmation e-mail that will be sent to the newly created user. |  [optional] |
|**email** | **String** | Email address. Must not be empty and must be unique within the service instance. |  |
|**firstName** | **String** | First name. |  |
|**lastName** | **String** | Last name. |  |
|**password** | **String** | User Password. If no value is provided, a default password is generated. |  [optional] |
|**identities** | [**List&lt;UserIdentityContract&gt;**](UserIdentityContract.md) | Collection of user identities. |  [optional] |
|**note** | **String** | Optional note about a user set by the administrator. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active. |  [optional] |



## Enum: ConfirmationEnum

| Name | Value |
|---- | -----|
| SIGNUP | &quot;signup&quot; |
| INVITE | &quot;invite&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| BLOCKED | &quot;blocked&quot; |
| PENDING | &quot;pending&quot; |
| DELETED | &quot;deleted&quot; |



