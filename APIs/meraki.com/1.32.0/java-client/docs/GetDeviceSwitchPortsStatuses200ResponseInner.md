

# GetDeviceSwitchPortsStatuses200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cdp** | [**GetDeviceSwitchPortsStatuses200ResponseInnerCdp**](GetDeviceSwitchPortsStatuses200ResponseInnerCdp.md) |  |  [optional] |
|**clientCount** | **Integer** | The number of clients connected through this port. |  [optional] |
|**duplex** | [**DuplexEnum**](#DuplexEnum) | The current duplex of a connected port. |  [optional] |
|**enabled** | **Boolean** | Whether the port is configured to be enabled. |  [optional] |
|**errors** | **List&lt;String&gt;** | All errors present on the port. |  [optional] |
|**isUplink** | **Boolean** | Whether the port is the switch&#39;s uplink. |  [optional] |
|**lldp** | [**GetDeviceSwitchPortsStatuses200ResponseInnerLldp**](GetDeviceSwitchPortsStatuses200ResponseInnerLldp.md) |  |  [optional] |
|**portId** | **String** | The string identifier of this port on the switch. This is commonly just the port number but may contain additional identifying information such as the slot and module-type if the port is located on a port module. |  [optional] |
|**powerUsageInWh** | **Float** | How much power (in watt-hours) has been delivered by this port during the timespan. |  [optional] |
|**securePort** | [**GetDeviceSwitchPortsStatuses200ResponseInnerSecurePort**](GetDeviceSwitchPortsStatuses200ResponseInnerSecurePort.md) |  |  [optional] |
|**speed** | [**SpeedEnum**](#SpeedEnum) | The current data transfer rate which the port is operating at. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current connection status of the port. |  [optional] |
|**trafficInKbps** | [**GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps**](GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.md) |  |  [optional] |
|**usageInKb** | [**GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb**](GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.md) |  |  [optional] |
|**warnings** | **List&lt;String&gt;** | All warnings present on the port. |  [optional] |



## Enum: DuplexEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| FULL | &quot;full&quot; |
| HALF | &quot;half&quot; |



## Enum: SpeedEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| _1_GBPS | &quot;1 Gbps&quot; |
| _10_GBPS | &quot;10 Gbps&quot; |
| _10_MBPS | &quot;10 Mbps&quot; |
| _100_GBPS | &quot;100 Gbps&quot; |
| _100_MBPS | &quot;100 Mbps&quot; |
| _2_5_GBPS | &quot;2.5 Gbps&quot; |
| _20_GBPS | &quot;20 Gbps&quot; |
| _40_GBPS | &quot;40 Gbps&quot; |
| _5_GBPS | &quot;5 Gbps&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CONNECTED | &quot;Connected&quot; |
| DISABLED | &quot;Disabled&quot; |
| DISCONNECTED | &quot;Disconnected&quot; |



