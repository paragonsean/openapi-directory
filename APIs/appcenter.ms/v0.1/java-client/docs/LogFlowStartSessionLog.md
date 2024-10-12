

# LogFlowStartSessionLog

Required explicit begin session log (a marker event for analytics service).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sessionId** | **UUID** | Session ID.  |  |
|**device** | [**AnalyticsGenericLogFlow200ResponseLogsInnerDevice**](AnalyticsGenericLogFlow200ResponseLogsInnerDevice.md) |  |  |
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
| START_SERVICE | &quot;start_service&quot; |
| CUSTOM_PROPERTIES | &quot;custom_properties&quot; |



