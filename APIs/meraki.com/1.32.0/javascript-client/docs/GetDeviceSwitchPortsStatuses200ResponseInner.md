# MerakiDashboardApi.GetDeviceSwitchPortsStatuses200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp** | [**GetDeviceSwitchPortsStatuses200ResponseInnerCdp**](GetDeviceSwitchPortsStatuses200ResponseInnerCdp.md) |  | [optional] 
**clientCount** | **Number** | The number of clients connected through this port. | [optional] 
**duplex** | **String** | The current duplex of a connected port. | [optional] 
**enabled** | **Boolean** | Whether the port is configured to be enabled. | [optional] 
**errors** | **[String]** | All errors present on the port. | [optional] 
**isUplink** | **Boolean** | Whether the port is the switch&#39;s uplink. | [optional] 
**lldp** | [**GetDeviceSwitchPortsStatuses200ResponseInnerLldp**](GetDeviceSwitchPortsStatuses200ResponseInnerLldp.md) |  | [optional] 
**portId** | **String** | The string identifier of this port on the switch. This is commonly just the port number but may contain additional identifying information such as the slot and module-type if the port is located on a port module. | [optional] 
**powerUsageInWh** | **Number** | How much power (in watt-hours) has been delivered by this port during the timespan. | [optional] 
**securePort** | [**GetDeviceSwitchPortsStatuses200ResponseInnerSecurePort**](GetDeviceSwitchPortsStatuses200ResponseInnerSecurePort.md) |  | [optional] 
**speed** | **String** | The current data transfer rate which the port is operating at. | [optional] 
**status** | **String** | The current connection status of the port. | [optional] 
**trafficInKbps** | [**GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps**](GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.md) |  | [optional] 
**usageInKb** | [**GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb**](GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.md) |  | [optional] 
**warnings** | **[String]** | All warnings present on the port. | [optional] 



## Enum: DuplexEnum


* `empty` (value: `""`)

* `full` (value: `"full"`)

* `half` (value: `"half"`)





## Enum: SpeedEnum


* `empty` (value: `""`)

* `1 Gbps` (value: `"1 Gbps"`)

* `10 Gbps` (value: `"10 Gbps"`)

* `10 Mbps` (value: `"10 Mbps"`)

* `100 Gbps` (value: `"100 Gbps"`)

* `100 Mbps` (value: `"100 Mbps"`)

* `2.5 Gbps` (value: `"2.5 Gbps"`)

* `20 Gbps` (value: `"20 Gbps"`)

* `40 Gbps` (value: `"40 Gbps"`)

* `5 Gbps` (value: `"5 Gbps"`)





## Enum: StatusEnum


* `Connected` (value: `"Connected"`)

* `Disabled` (value: `"Disabled"`)

* `Disconnected` (value: `"Disconnected"`)




