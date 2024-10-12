

# SmtpMsa

Configuration for communication with an SMTP service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | The hostname of the SMTP service. Required. |  [optional] |
|**password** | **String** | The password that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses. |  [optional] |
|**port** | **Integer** | The port of the SMTP service. Required. |  [optional] |
|**securityMode** | [**SecurityModeEnum**](#SecurityModeEnum) | The protocol that will be used to secure communication with the SMTP service. Required. |  [optional] |
|**username** | **String** | The username that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses. |  [optional] |



## Enum: SecurityModeEnum

| Name | Value |
|---- | -----|
| SECURITY_MODE_UNSPECIFIED | &quot;securityModeUnspecified&quot; |
| NONE | &quot;none&quot; |
| SSL | &quot;ssl&quot; |
| STARTTLS | &quot;starttls&quot; |



