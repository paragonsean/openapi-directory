# StorSimple8000SeriesManagementClient.NetworkAdapters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interfaceId** | **String** | The ID of the network adapter. | 
**isDefault** | **Boolean** | Value indicating whether this instance is default. | [optional] 
**iscsiAndCloudStatus** | **String** | Value indicating cloud and ISCSI status of network adapter. | 
**mode** | **String** | The mode of network adapter, either IPv4, IPv6 or both. | 
**netInterfaceStatus** | **String** | Value indicating status of network adapter. | 
**nicIpv4Settings** | [**NicIPv4**](NicIPv4.md) |  | [optional] 
**nicIpv6Settings** | [**NicIPv6**](NicIPv6.md) |  | [optional] 
**speed** | **Number** | The speed of the network adapter. | [optional] 



## Enum: InterfaceIdEnum


* `Invalid` (value: `"Invalid"`)

* `Data0` (value: `"Data0"`)

* `Data1` (value: `"Data1"`)

* `Data2` (value: `"Data2"`)

* `Data3` (value: `"Data3"`)

* `Data4` (value: `"Data4"`)

* `Data5` (value: `"Data5"`)





## Enum: IscsiAndCloudStatusEnum


* `Disabled` (value: `"Disabled"`)

* `IscsiEnabled` (value: `"IscsiEnabled"`)

* `CloudEnabled` (value: `"CloudEnabled"`)

* `IscsiAndCloudEnabled` (value: `"IscsiAndCloudEnabled"`)





## Enum: ModeEnum


* `Invalid` (value: `"Invalid"`)

* `IPV4` (value: `"IPV4"`)

* `IPV6` (value: `"IPV6"`)

* `BOTH` (value: `"BOTH"`)





## Enum: NetInterfaceStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




