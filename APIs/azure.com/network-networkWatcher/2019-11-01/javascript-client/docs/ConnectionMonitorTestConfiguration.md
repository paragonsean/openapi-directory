# NetworkManagementClient.ConnectionMonitorTestConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**httpConfiguration** | [**ConnectionMonitorHttpConfiguration**](ConnectionMonitorHttpConfiguration.md) |  | [optional] 
**icmpConfiguration** | [**ConnectionMonitorIcmpConfiguration**](ConnectionMonitorIcmpConfiguration.md) |  | [optional] 
**name** | **String** | The name of the connection monitor test configuration. | 
**preferredIPVersion** | **String** | The preferred IP version to use in test evaluation. The connection monitor may choose to use a different version depending on other parameters. | [optional] 
**protocol** | **String** | The protocol to use in test evaluation. | 
**successThreshold** | [**ConnectionMonitorSuccessThreshold**](ConnectionMonitorSuccessThreshold.md) |  | [optional] 
**tcpConfiguration** | [**ConnectionMonitorTcpConfiguration**](ConnectionMonitorTcpConfiguration.md) |  | [optional] 
**testFrequencySec** | **Number** | The frequency of test evaluation, in seconds. | [optional] 



## Enum: PreferredIPVersionEnum


* `IPv4` (value: `"IPv4"`)

* `IPv6` (value: `"IPv6"`)





## Enum: ProtocolEnum


* `Tcp` (value: `"Tcp"`)

* `Http` (value: `"Http"`)

* `Icmp` (value: `"Icmp"`)




