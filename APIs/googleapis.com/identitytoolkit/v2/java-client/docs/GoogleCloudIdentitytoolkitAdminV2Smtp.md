

# GoogleCloudIdentitytoolkitAdminV2Smtp

Configuration for SMTP relay

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | SMTP relay host |  [optional] |
|**password** | **String** | SMTP relay password |  [optional] |
|**port** | **Integer** | SMTP relay port |  [optional] |
|**securityMode** | [**SecurityModeEnum**](#SecurityModeEnum) | SMTP security mode. |  [optional] |
|**senderEmail** | **String** | Sender email for the SMTP relay |  [optional] |
|**username** | **String** | SMTP relay username |  [optional] |



## Enum: SecurityModeEnum

| Name | Value |
|---- | -----|
| SECURITY_MODE_UNSPECIFIED | &quot;SECURITY_MODE_UNSPECIFIED&quot; |
| SSL | &quot;SSL&quot; |
| START_TLS | &quot;START_TLS&quot; |



