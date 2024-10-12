# AwsIoTWireless.UpdateLogLevelsByResourceTypesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultLogLevel** | **String** | The log level for a log message. The log levels can be disabled, or set to &lt;code&gt;ERROR&lt;/code&gt; to display less verbose logs containing only error information, or to &lt;code&gt;INFO&lt;/code&gt; for more detailed logs. | [optional] 
**wirelessDeviceLogOptions** | [**[WirelessDeviceLogOption]**](WirelessDeviceLogOption.md) | The list of wireless device log options. | [optional] 
**wirelessGatewayLogOptions** | [**[WirelessGatewayLogOption]**](WirelessGatewayLogOption.md) | The list of wireless gateway log options. | [optional] 



## Enum: DefaultLogLevelEnum


* `INFO` (value: `"INFO"`)

* `ERROR` (value: `"ERROR"`)

* `DISABLED` (value: `"DISABLED"`)




