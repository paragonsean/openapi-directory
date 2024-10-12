

# UserCreateOrUpdateRequestProperties

Parameters supplied to the Create User operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appType** | [**AppTypeEnum**](#AppTypeEnum) | Determines the type of application which send the create user request. Default is old publisher portal. |  [optional] |
|**confirmation** | [**ConfirmationEnum**](#ConfirmationEnum) | Determines the type of confirmation e-mail that will be sent to the newly created user. |  [optional] |
|**email** | **String** | Email address. Must not be empty and must be unique within the service instance. |  |
|**firstName** | **String** | First name. |  |
|**lastName** | **String** | Last name. |  |
|**password** | **String** | User Password. If no value is provided, a default password is generated. |  [optional] |



## Enum: AppTypeEnum

| Name | Value |
|---- | -----|
| DEVELOPER_PORTAL | &quot;developerPortal&quot; |



## Enum: ConfirmationEnum

| Name | Value |
|---- | -----|
| SIGNUP | &quot;signup&quot; |
| INVITE | &quot;invite&quot; |



