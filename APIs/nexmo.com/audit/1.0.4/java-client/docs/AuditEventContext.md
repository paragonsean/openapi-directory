

# AuditEventContext

A valid JSON object with information detailing the context of the audit event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | UUID of the app that was created |  [optional] |
|**created** | [**ContextAppCreateCreated**](ContextAppCreateCreated.md) |  |  [optional] |
|**account** | **String** | Which account the number is associated with |  [optional] |
|**applicationId** | **String** | UUID of the app the number is being linked/unlinked to |  [optional] |
|**country** | **String** | The country of the number |  [optional] |
|**msisdn** | **String** | The phone number linked/unlinked to your application |  [optional] |
|**http** | **String** | The URL of the endpoint the number has been forwarded to |  [optional] |
|**voiceType** | [**VoiceTypeEnum**](#VoiceTypeEnum) | The type of endpoint the number has been forwarded to |  [optional] |
|**voiceValue** | **String** | The value of the endpoint the number has been forwarded to |  [optional] |



## Enum: VoiceTypeEnum

| Name | Value |
|---- | -----|
| TEL | &quot;tel&quot; |
| SIP | &quot;sip&quot; |
| VXML | &quot;vxml&quot; |
| APP | &quot;app&quot; |



