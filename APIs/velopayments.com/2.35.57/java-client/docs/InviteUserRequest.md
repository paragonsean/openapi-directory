

# InviteUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | the email address of the invited user |  |
|**entityId** | **UUID** | The payorId or payeeId or null if the user is a backoffice admin  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**mfaType** | [**MfaTypeEnum**](#MfaTypeEnum) | &lt;p&gt;The MFA type that the user will use&lt;/p&gt; &lt;p&gt;The type may be conditional on the role(s) the user has&lt;/p&gt;  |  |
|**primaryContactNumber** | **String** | The main contact number for the user  |  |
|**roles** | **List&lt;String&gt;** | The role(s) for the user The role must exist The role can be a custom role or a system role but the invoker must have the permissions to assign the role System roles are: velo.backoffice.admin, velo.payor.master_admin, velo.payor.admin, velo.payor.support, velo.payee.admin, velo.payee.support  |  |
|**secondaryContactNumber** | **String** | The secondary contact number for the user  |  [optional] |
|**smsNumber** | **String** | The phone number of a device that the user can receive sms messages on  |  |
|**userType** | [**UserTypeEnum**](#UserTypeEnum) | Will default to PAYOR if not provided but entityId is provided |  [optional] |
|**verificationCode** | **String** | Optional property that MUST be suppied when manually verifying a user The user&#39;s smsNumber is registered via a separate endpoint and an OTP sent to them  |  [optional] |



## Enum: MfaTypeEnum

| Name | Value |
|---- | -----|
| SMS | &quot;SMS&quot; |
| YUBIKEY | &quot;YUBIKEY&quot; |
| TOTP | &quot;TOTP&quot; |



## Enum: UserTypeEnum

| Name | Value |
|---- | -----|
| BACKOFFICE | &quot;BACKOFFICE&quot; |
| PAYOR | &quot;PAYOR&quot; |
| PAYEE | &quot;PAYEE&quot; |



