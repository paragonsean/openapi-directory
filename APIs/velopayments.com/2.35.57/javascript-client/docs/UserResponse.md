# VeloPaymentsApis.UserResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**companyName** | **String** | The payor or payee company name or null if the user is not a payor or payee user  | [optional] 
**email** | **String** | the email address of the user | [optional] 
**entityId** | **String** | The payorId or payeeId or null if the user is not a payor or payee user  | [optional] 
**firstName** | **String** |  | [optional] 
**id** | **String** | The id of the user | [optional] 
**lastName** | **String** |  | [optional] 
**lockedOut** | **Boolean** | If true the user is currently locked out and unable to log in | [optional] 
**lockedOutTimestamp** | **Date** | A timestamp showing when the user was locked out If null then the user is not currently locked out  | [optional] 
**mfaStatus** | **String** | The status of the MFA device | [optional] 
**mfaType** | **String** | The type of the MFA device | [optional] 
**primaryContactNumber** | **String** | The main contact number for the user  | [optional] 
**roles** | [**[Role]**](Role.md) | The role(s) for the user  | [optional] 
**secondaryContactNumber** | **String** | The secondary contact number for the user  | [optional] 
**smsNumber** | **String** | The phone number of a device that the user can receive sms messages on  | [optional] 
**status** | **String** | The status of the user when the user has been invited but not yet enrolled they will have a PENDING status  | [optional] 
**userType** | **String** | Indicates the type of user. Could be BACKOFFICE, PAYOR or PAYEE. | [optional] 



## Enum: MfaStatusEnum


* `REGISTERED` (value: `"REGISTERED"`)

* `UNREGISTERED` (value: `"UNREGISTERED"`)





## Enum: MfaTypeEnum


* `SMS` (value: `"SMS"`)

* `YUBIKEY` (value: `"YUBIKEY"`)

* `TOTP` (value: `"TOTP"`)





## Enum: StatusEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)

* `PENDING` (value: `"PENDING"`)





## Enum: UserTypeEnum


* `BACKOFFICE` (value: `"BACKOFFICE"`)

* `PAYOR` (value: `"PAYOR"`)

* `PAYEE` (value: `"PAYEE"`)




