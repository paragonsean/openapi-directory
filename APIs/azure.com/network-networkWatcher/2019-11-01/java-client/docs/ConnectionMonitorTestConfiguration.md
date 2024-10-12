

# ConnectionMonitorTestConfiguration

Describes a connection monitor test configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**httpConfiguration** | [**ConnectionMonitorHttpConfiguration**](ConnectionMonitorHttpConfiguration.md) |  |  [optional] |
|**icmpConfiguration** | [**ConnectionMonitorIcmpConfiguration**](ConnectionMonitorIcmpConfiguration.md) |  |  [optional] |
|**name** | **String** | The name of the connection monitor test configuration. |  |
|**preferredIPVersion** | [**PreferredIPVersionEnum**](#PreferredIPVersionEnum) | The preferred IP version to use in test evaluation. The connection monitor may choose to use a different version depending on other parameters. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The protocol to use in test evaluation. |  |
|**successThreshold** | [**ConnectionMonitorSuccessThreshold**](ConnectionMonitorSuccessThreshold.md) |  |  [optional] |
|**tcpConfiguration** | [**ConnectionMonitorTcpConfiguration**](ConnectionMonitorTcpConfiguration.md) |  |  [optional] |
|**testFrequencySec** | **Integer** | The frequency of test evaluation, in seconds. |  [optional] |



## Enum: PreferredIPVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;Tcp&quot; |
| HTTP | &quot;Http&quot; |
| ICMP | &quot;Icmp&quot; |



