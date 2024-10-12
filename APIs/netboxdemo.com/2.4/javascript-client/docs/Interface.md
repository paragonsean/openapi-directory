# NetBoxApi.Interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuitTermination** | [**InterfaceCircuitTermination**](InterfaceCircuitTermination.md) |  | [optional] 
**description** | **String** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**enabled** | **Boolean** |  | [optional] 
**formFactor** | [**FormFactor**](FormFactor.md) |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**interfaceConnection** | **String** |  | [optional] [readonly] 
**isConnected** | **String** |  | [optional] [readonly] 
**lag** | [**NestedInterface**](NestedInterface.md) |  | [optional] 
**macAddress** | **String** |  | [optional] 
**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management | [optional] 
**mode** | [**Mode**](Mode.md) |  | [optional] 
**mtu** | **Number** |  | [optional] 
**name** | **String** |  | 
**taggedVlans** | [**[InterfaceVLAN]**](InterfaceVLAN.md) |  | [optional] 
**tags** | **[String]** |  | [optional] 
**untaggedVlan** | [**InterfaceVLAN**](InterfaceVLAN.md) |  | [optional] 


