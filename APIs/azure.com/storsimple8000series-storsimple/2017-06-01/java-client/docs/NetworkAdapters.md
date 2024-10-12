

# NetworkAdapters

Represents the network adapter on device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interfaceId** | [**InterfaceIdEnum**](#InterfaceIdEnum) | The ID of the network adapter. |  |
|**isDefault** | **Boolean** | Value indicating whether this instance is default. |  [optional] |
|**iscsiAndCloudStatus** | [**IscsiAndCloudStatusEnum**](#IscsiAndCloudStatusEnum) | Value indicating cloud and ISCSI status of network adapter. |  |
|**mode** | [**ModeEnum**](#ModeEnum) | The mode of network adapter, either IPv4, IPv6 or both. |  |
|**netInterfaceStatus** | [**NetInterfaceStatusEnum**](#NetInterfaceStatusEnum) | Value indicating status of network adapter. |  |
|**nicIpv4Settings** | [**NicIPv4**](NicIPv4.md) |  |  [optional] |
|**nicIpv6Settings** | [**NicIPv6**](NicIPv6.md) |  |  [optional] |
|**speed** | **Long** | The speed of the network adapter. |  [optional] |



## Enum: InterfaceIdEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DATA0 | &quot;Data0&quot; |
| DATA1 | &quot;Data1&quot; |
| DATA2 | &quot;Data2&quot; |
| DATA3 | &quot;Data3&quot; |
| DATA4 | &quot;Data4&quot; |
| DATA5 | &quot;Data5&quot; |



## Enum: IscsiAndCloudStatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ISCSI_ENABLED | &quot;IscsiEnabled&quot; |
| CLOUD_ENABLED | &quot;CloudEnabled&quot; |
| ISCSI_AND_CLOUD_ENABLED | &quot;IscsiAndCloudEnabled&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IPV4 | &quot;IPV4&quot; |
| IPV6 | &quot;IPV6&quot; |
| BOTH | &quot;BOTH&quot; |



## Enum: NetInterfaceStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



