

# SmartMeDeviceConfigurationContainer

API Container class for the meter configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceEncryptionKey** | **String** | The encryption key used to decrypt messages received from an external meter (used only for the smart-me modules) |  [optional] |
|**devicePinCode** | **String** | PIN code to enter on a external meter (e.g. for the FNN meters) |  [optional] |
|**dnsUpdateState** | [**DnsUpdateStateEnum**](#DnsUpdateStateEnum) | Configuration of the dynamic DNS service. More information: http://wiki.smart-me.com/index.php/Dynamisches_DNS |  [optional] |
|**enableModbusTcp** | **Boolean** | Enables or disables Modbus TCP (if the meter supports it). |  [optional] |
|**id** | **String** | The ID of the device |  [optional] |
|**inputConfiguration** | [**List&lt;InputConfigurationContainer&gt;**](InputConfigurationContainer.md) | The configuration for the intput outputs |  [optional] |
|**outputConfiguration** | [**List&lt;OutputConfigurationContainer&gt;**](OutputConfigurationContainer.md) | The configuration for the external outputs |  [optional] |
|**showReactiveEnergy** | **Boolean** | Shows the reactive energy values (if the meter supports it). |  [optional] |
|**switchConfiguration** | [**List&lt;SwitchConfigurationContainer&gt;**](SwitchConfigurationContainer.md) | The configuration for the phase switches |  [optional] |
|**uploadInterval** | [**UploadIntervalEnum**](#UploadIntervalEnum) | Number of seconds the device will upload the data. For smaller values maybe a professional license is needed. |  [optional] |



## Enum: DnsUpdateStateEnum

| Name | Value |
|---- | -----|
| NO_UPDATE | &quot;NoUpdate&quot; |
| DNS_UPDATE_PUBLIC_IP | &quot;DnsUpdatePublicIp&quot; |
| DNS_UPDATE_INTERNAL_IP | &quot;DnsUpdateInternalIp&quot; |



## Enum: UploadIntervalEnum

| Name | Value |
|---- | -----|
| _1S | &quot;UploadInterval_1s&quot; |
| _5S | &quot;UploadInterval_5s&quot; |
| _10S | &quot;UploadInterval_10s&quot; |
| _30S | &quot;UploadInterval_30s&quot; |
| _60S | &quot;UploadInterval_60s&quot; |
| _5MIN | &quot;UploadInterval_5min&quot; |
| _15MIN | &quot;UploadInterval_15min&quot; |
| _30MIN | &quot;UploadInterval_30min&quot; |
| _60MIN | &quot;UploadInterval_60min&quot; |
| _6H | &quot;UploadInterval_6h&quot; |
| _12H | &quot;UploadInterval_12h&quot; |
| _24H | &quot;UploadInterval_24h&quot; |



