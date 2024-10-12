# ApiManagementClient.UserEntityBaseParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identities** | [**[UserIdentityContract]**](UserIdentityContract.md) | Collection of user identities. | [optional] 
**note** | **String** | Optional note about a user set by the administrator. | [optional] 
**state** | **String** | Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active. | [optional] [default to &#39;active&#39;]



## Enum: StateEnum


* `active` (value: `"active"`)

* `blocked` (value: `"blocked"`)

* `pending` (value: `"pending"`)

* `deleted` (value: `"deleted"`)




