

# UpdateLogLevelsByResourceTypesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultLogLevel** | [**DefaultLogLevelEnum**](#DefaultLogLevelEnum) | The log level for a log message. The log levels can be disabled, or set to &lt;code&gt;ERROR&lt;/code&gt; to display less verbose logs containing only error information, or to &lt;code&gt;INFO&lt;/code&gt; for more detailed logs. |  [optional] |
|**wirelessDeviceLogOptions** | [**List&lt;WirelessDeviceLogOption&gt;**](WirelessDeviceLogOption.md) | The list of wireless device log options. |  [optional] |
|**wirelessGatewayLogOptions** | [**List&lt;WirelessGatewayLogOption&gt;**](WirelessGatewayLogOption.md) | The list of wireless gateway log options. |  [optional] |



## Enum: DefaultLogLevelEnum

| Name | Value |
|---- | -----|
| INFO | &quot;INFO&quot; |
| ERROR | &quot;ERROR&quot; |
| DISABLED | &quot;DISABLED&quot; |



