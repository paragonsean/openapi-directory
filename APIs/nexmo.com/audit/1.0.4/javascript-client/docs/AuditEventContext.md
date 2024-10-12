# AuditApi.AuditEventContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | UUID of the app that was created | [optional] 
**created** | [**ContextAppCreateCreated**](ContextAppCreateCreated.md) |  | [optional] 
**account** | **String** | Which account the number is associated with | [optional] 
**applicationId** | **String** | UUID of the app the number is being linked/unlinked to | [optional] 
**country** | **String** | The country of the number | [optional] 
**msisdn** | **String** | The phone number linked/unlinked to your application | [optional] 
**http** | **String** | The URL of the endpoint the number has been forwarded to | [optional] 
**voiceType** | **String** | The type of endpoint the number has been forwarded to | [optional] 
**voiceValue** | **String** | The value of the endpoint the number has been forwarded to | [optional] 



## Enum: VoiceTypeEnum


* `tel` (value: `"tel"`)

* `sip` (value: `"sip"`)

* `vxml` (value: `"vxml"`)

* `app` (value: `"app"`)




