# ApiManagementClient.UserCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | Email address. Must not be empty and must be unique within the service instance. | 
**firstName** | **String** | First name. | 
**lastName** | **String** | Last name. | 
**note** | **String** | Optional note about a user set by the administrator. | [optional] 
**password** | **String** | User Password. | 
**state** | **String** | Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active. | [optional] [default to &#39;Active&#39;]



## Enum: StateEnum


* `Active` (value: `"Active"`)

* `Blocked` (value: `"Blocked"`)




