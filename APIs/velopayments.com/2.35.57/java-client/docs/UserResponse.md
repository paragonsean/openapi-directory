

# UserResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**companyName** | **String** | The payor or payee company name or null if the user is not a payor or payee user  |  [optional] |
|**email** | **String** | the email address of the user |  [optional] |
|**entityId** | **UUID** | The payorId or payeeId or null if the user is not a payor or payee user  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**id** | **UUID** | The id of the user |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**lockedOut** | **Boolean** | If true the user is currently locked out and unable to log in |  [optional] |
|**lockedOutTimestamp** | **OffsetDateTime** | A timestamp showing when the user was locked out If null then the user is not currently locked out  |  [optional] |
|**mfaStatus** | [**MfaStatusEnum**](#MfaStatusEnum) | The status of the MFA device |  [optional] |
|**mfaType** | [**MfaTypeEnum**](#MfaTypeEnum) | The type of the MFA device |  [optional] |
|**primaryContactNumber** | **String** | The main contact number for the user  |  [optional] |
|**roles** | [**List&lt;Role&gt;**](Role.md) | The role(s) for the user  |  [optional] |
|**secondaryContactNumber** | **String** | The secondary contact number for the user  |  [optional] |
|**smsNumber** | **String** | The phone number of a device that the user can receive sms messages on  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the user when the user has been invited but not yet enrolled they will have a PENDING status  |  [optional] |
|**userType** | [**UserTypeEnum**](#UserTypeEnum) | Indicates the type of user. Could be BACKOFFICE, PAYOR or PAYEE. |  [optional] |



## Enum: MfaStatusEnum

| Name | Value |
|---- | -----|
| REGISTERED | &quot;REGISTERED&quot; |
| UNREGISTERED | &quot;UNREGISTERED&quot; |



## Enum: MfaTypeEnum

| Name | Value |
|---- | -----|
| SMS | &quot;SMS&quot; |
| YUBIKEY | &quot;YUBIKEY&quot; |
| TOTP | &quot;TOTP&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: UserTypeEnum

| Name | Value |
|---- | -----|
| BACKOFFICE | &quot;BACKOFFICE&quot; |
| PAYOR | &quot;PAYOR&quot; |
| PAYEE | &quot;PAYEE&quot; |



