# AppCenterClient.InternalUserSignupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The full name of the user. Might for example be first and last name | 
**email** | **String** | The email address of the user | 
**externalProvider** | **String** | The name of the external auth provider | [optional] 
**externalUserId** | **String** | The user ID given by the external provider | [optional] 
**id** | **String** | The unique id (UUID) of the user | 
**name** | **String** | The unique name that is used to identify the user. | 
**status** | **String** | The current status of the user record after signup | [optional] 



## Enum: StatusEnum


* `Complete` (value: `"Complete"`)

* `NeedsVerification` (value: `"NeedsVerification"`)




