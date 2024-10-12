

# ContextNumberUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | The country of the number |  [optional] |
|**http** | **String** | The URL of the endpoint the number has been forwarded to |  [optional] |
|**msisdn** | **String** | The phone number linked/unlinked to your application |  [optional] |
|**voiceType** | [**VoiceTypeEnum**](#VoiceTypeEnum) | The type of endpoint the number has been forwarded to |  [optional] |
|**voiceValue** | **String** | The value of the endpoint the number has been forwarded to |  [optional] |



## Enum: VoiceTypeEnum

| Name | Value |
|---- | -----|
| TEL | &quot;tel&quot; |
| SIP | &quot;sip&quot; |
| VXML | &quot;vxml&quot; |
| APP | &quot;app&quot; |



