# ApiManagementClient.UserContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | Email address. | [optional] 
**firstName** | **String** | First name. | [optional] 
**id** | **String** | User identifier path. | [optional] 
**identities** | [**[UserIdentityContract]**](UserIdentityContract.md) | Collection of user identities. | [optional] [readonly] 
**lastName** | **String** | Last name. | [optional] 
**note** | **String** | Administrator&#39;s note about given user. | [optional] 
**registrationDate** | **Date** | Date of user registration. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | [optional] 
**state** | **String** | User state. | [optional] 



## Enum: StateEnum


* `Active` (value: `"Active"`)

* `Blocked` (value: `"Blocked"`)




