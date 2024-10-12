# ApiManagementClient.UserCreateOrUpdateRequestProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appType** | **String** | Determines the type of application which send the create user request. Default is legacy portal. | [optional] 
**confirmation** | **String** | Determines the type of confirmation e-mail that will be sent to the newly created user. | [optional] 
**email** | **String** | Email address. Must not be empty and must be unique within the service instance. | 
**firstName** | **String** | First name. | 
**lastName** | **String** | Last name. | 
**password** | **String** | User Password. If no value is provided, a default password is generated. | [optional] 



## Enum: AppTypeEnum


* `portal` (value: `"portal"`)

* `developerPortal` (value: `"developerPortal"`)





## Enum: ConfirmationEnum


* `signup` (value: `"signup"`)

* `invite` (value: `"invite"`)




