# ApiManagementClient.UserContractProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | Email address. | [optional] 
**firstName** | **String** | First name. | [optional] 
**groups** | **[Object]** | Collection of groups user is part of. | [optional] [readonly] 
**lastName** | **String** | Last name. | [optional] 
**registrationDate** | **Date** | Date of user registration. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 
**identities** | [**[UserIdentityContract]**](UserIdentityContract.md) | Collection of user identities. | [optional] [readonly] 
**note** | **String** | Optional note about a user set by the administrator. | [optional] 
**state** | **String** | Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active. | [optional] [default to &#39;active&#39;]



## Enum: StateEnum


* `active` (value: `"active"`)

* `blocked` (value: `"blocked"`)

* `pending` (value: `"pending"`)

* `deleted` (value: `"deleted"`)




