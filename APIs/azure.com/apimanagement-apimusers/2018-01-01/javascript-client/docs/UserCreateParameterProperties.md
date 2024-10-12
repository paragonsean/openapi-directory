# ApiManagementClient.UserCreateParameterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation** | **String** | Determines the type of confirmation e-mail that will be sent to the newly created user. | [optional] 
**email** | **String** | Email address. Must not be empty and must be unique within the service instance. | 
**firstName** | **String** | First name. | 
**lastName** | **String** | Last name. | 
**password** | **String** | User Password. If no value is provided, a default password is generated. | [optional] 
**identities** | [**[UserIdentityContract]**](UserIdentityContract.md) | Collection of user identities. | [optional] 
**note** | **String** | Optional note about a user set by the administrator. | [optional] 
**state** | **String** | Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active. | [optional] [default to &#39;active&#39;]



## Enum: ConfirmationEnum


* `signup` (value: `"signup"`)

* `invite` (value: `"invite"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `blocked` (value: `"blocked"`)

* `pending` (value: `"pending"`)

* `deleted` (value: `"deleted"`)




