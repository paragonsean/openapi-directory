

# StartServiceLog

Describe a AppCenter.Start API call from the SDK.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**services** | **List&lt;String&gt;** | The list of services of the AppCenter Start API call. |  [optional] |
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
| PUSH_INSTALLATION | &quot;push_installation&quot; |
| START_SERVICE | &quot;start_service&quot; |
| CUSTOM_PROPERTIES | &quot;custom_properties&quot; |



