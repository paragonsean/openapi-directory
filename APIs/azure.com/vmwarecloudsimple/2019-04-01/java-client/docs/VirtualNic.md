

# VirtualNic

Virtual NIC model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customization** | [**GuestOSNICCustomization**](GuestOSNICCustomization.md) |  |  [optional] |
|**ipAddresses** | **List&lt;String&gt;** | NIC ip address |  [optional] |
|**macAddress** | **String** | NIC MAC address |  [optional] |
|**network** | [**VirtualNetwork**](VirtualNetwork.md) |  |  |
|**nicType** | [**NicTypeEnum**](#NicTypeEnum) | NIC type |  |
|**powerOnBoot** | **Boolean** | Is NIC powered on/off on boot |  [optional] |
|**virtualNicId** | **String** | NIC id |  [optional] |
|**virtualNicName** | **String** | NIC name |  [optional] [readonly] |



## Enum: NicTypeEnum

| Name | Value |
|---- | -----|
| E1000 | &quot;E1000&quot; |
| E1000_E | &quot;E1000E&quot; |
| PCNET32 | &quot;PCNET32&quot; |
| VMXNET | &quot;VMXNET&quot; |
| VMXNET2 | &quot;VMXNET2&quot; |
| VMXNET3 | &quot;VMXNET3&quot; |



