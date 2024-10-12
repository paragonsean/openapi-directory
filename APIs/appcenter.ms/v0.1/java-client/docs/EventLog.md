

# EventLog

Event log.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | Unique identifier for this event.  |  |
|**name** | **String** | Name of the event.  |  |
|**sessionId** | **UUID** | Session ID.  |  |
|**properties** | **Map&lt;String, String&gt;** | Additional key/value pair parameters.  |  [optional] |
|**device** | [**Object**](Object.md) | Device characteristics. |  |
|**installId** | **UUID** | Install ID.  |  |
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



