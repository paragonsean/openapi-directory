

# GetDeviceSwitchPortsStatuses200ResponseInnerCdp

The Cisco Discovery Protocol (CDP) information of the connected device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Contains network addresses of both receiving and sending devices. |  [optional] |
|**capabilities** | **String** | Identifies the device type, which indicates the functional capabilities of the device. |  [optional] |
|**deviceId** | **String** | Identifies the device name. |  [optional] |
|**managementAddress** | **String** | The device&#39;s management IP. |  [optional] |
|**nativeVlan** | **Integer** | Indicates, per interface, the assumed VLAN for untagged packets on the interface. |  [optional] |
|**platform** | **String** | Identifies the hardware platform of the device. |  [optional] |
|**portId** | **String** | Identifies the port from which the CDP packet was sent. |  [optional] |
|**systemName** | **String** | The system name. |  [optional] |
|**version** | **String** | Contains the device software release information. |  [optional] |
|**vtpManagementDomain** | **String** | Advertises the configured VLAN Trunking Protocl (VTP)-management-domain name of the system. |  [optional] |



