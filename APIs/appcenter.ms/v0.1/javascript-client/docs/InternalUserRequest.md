# AppCenterClient.InternalUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appInvitation** | **String** | The token of the app invitation which lead to signup | [optional] 
**avatarUrl** | **String** | The avatar URL of the user | [optional] 
**displayName** | **String** | The full name of the user. Might for example be first and last name | [optional] 
**email** | **String** | The email address of the user | 
**name** | **String** | The unique name that is used to identify the user. | 
**organizationInvitation** | **String** | The token of the organization invitation which lead to signup | [optional] 
**password** | **String** | The password of the user. Needs to be at least 8 characters long and contain at least one lower- and one uppercase letter. | 
**portalSubdomain** | **String** | The sub-domain of the portal from which this request was made. Will be used to build the invitation link. | [optional] 
**testerInvitation** | **String** | The token of the test invitation which lead to signup | [optional] 



## Enum: PortalSubdomainEnum


* `install.` (value: `"install."`)




