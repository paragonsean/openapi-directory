

# GenericLogDiagnostics

Generic log.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**device** | [**AnalyticsGenericLogFlow200ResponseLogsInnerDevice**](AnalyticsGenericLogFlow200ResponseLogsInnerDevice.md) |  |  |
|**eventId** | **String** | Event ID.  |  [optional] |
|**eventName** | **String** | Event name.  |  [optional] |
|**installId** | **UUID** | Install ID.  |  |
|**messageId** | **String** | Message ID.  |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | event specific properties.  |  [optional] |
|**sessionId** | **UUID** | Session ID.  |  [optional] |
|**timestamp** | **OffsetDateTime** | Log creation timestamp.  |  |
|**type** | [**TypeEnum**](#TypeEnum) | Log type.  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EVENT | &quot;event&quot; |
| PAGE | &quot;page&quot; |
| START_SESSION | &quot;start_session&quot; |
| ERROR | &quot;error&quot; |
| PUSH_INSTALLATION | &quot;push_installation&quot; |
| START_SERVICE | &quot;start_service&quot; |
| CUSTOM_PROPERTIES | &quot;custom_properties&quot; |



