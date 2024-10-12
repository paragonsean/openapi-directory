

# GoogleCloudIdentitytoolkitAdminV2SendEmail

Options for email sending.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackUri** | **String** | action url in email template. |  [optional] |
|**changeEmailTemplate** | [**GoogleCloudIdentitytoolkitAdminV2EmailTemplate**](GoogleCloudIdentitytoolkitAdminV2EmailTemplate.md) |  |  [optional] |
|**dnsInfo** | [**GoogleCloudIdentitytoolkitAdminV2DnsInfo**](GoogleCloudIdentitytoolkitAdminV2DnsInfo.md) |  |  [optional] |
|**legacyResetPasswordTemplate** | [**GoogleCloudIdentitytoolkitAdminV2EmailTemplate**](GoogleCloudIdentitytoolkitAdminV2EmailTemplate.md) |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | The method used for sending an email. |  [optional] |
|**resetPasswordTemplate** | [**GoogleCloudIdentitytoolkitAdminV2EmailTemplate**](GoogleCloudIdentitytoolkitAdminV2EmailTemplate.md) |  |  [optional] |
|**revertSecondFactorAdditionTemplate** | [**GoogleCloudIdentitytoolkitAdminV2EmailTemplate**](GoogleCloudIdentitytoolkitAdminV2EmailTemplate.md) |  |  [optional] |
|**smtp** | [**GoogleCloudIdentitytoolkitAdminV2Smtp**](GoogleCloudIdentitytoolkitAdminV2Smtp.md) |  |  [optional] |
|**verifyEmailTemplate** | [**GoogleCloudIdentitytoolkitAdminV2EmailTemplate**](GoogleCloudIdentitytoolkitAdminV2EmailTemplate.md) |  |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| METHOD_UNSPECIFIED | &quot;METHOD_UNSPECIFIED&quot; |
| DEFAULT | &quot;DEFAULT&quot; |
| CUSTOM_SMTP | &quot;CUSTOM_SMTP&quot; |



