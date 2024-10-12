# VMwareCloudSimple.VirtualNic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customization** | [**GuestOSNICCustomization**](GuestOSNICCustomization.md) |  | [optional] 
**ipAddresses** | **[String]** | NIC ip address | [optional] 
**macAddress** | **String** | NIC MAC address | [optional] 
**network** | [**VirtualNetwork**](VirtualNetwork.md) |  | 
**nicType** | **String** | NIC type | 
**powerOnBoot** | **Boolean** | Is NIC powered on/off on boot | [optional] 
**virtualNicId** | **String** | NIC id | [optional] 
**virtualNicName** | **String** | NIC name | [optional] [readonly] 



## Enum: NicTypeEnum


* `E1000` (value: `"E1000"`)

* `E1000E` (value: `"E1000E"`)

* `PCNET32` (value: `"PCNET32"`)

* `VMXNET` (value: `"VMXNET"`)

* `VMXNET2` (value: `"VMXNET2"`)

* `VMXNET3` (value: `"VMXNET3"`)




