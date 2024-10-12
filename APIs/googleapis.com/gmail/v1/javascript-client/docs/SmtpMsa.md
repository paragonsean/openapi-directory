# GmailApi.SmtpMsa

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **String** | The hostname of the SMTP service. Required. | [optional] 
**password** | **String** | The password that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses. | [optional] 
**port** | **Number** | The port of the SMTP service. Required. | [optional] 
**securityMode** | **String** | The protocol that will be used to secure communication with the SMTP service. Required. | [optional] 
**username** | **String** | The username that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses. | [optional] 



## Enum: SecurityModeEnum


* `securityModeUnspecified` (value: `"securityModeUnspecified"`)

* `none` (value: `"none"`)

* `ssl` (value: `"ssl"`)

* `starttls` (value: `"starttls"`)




