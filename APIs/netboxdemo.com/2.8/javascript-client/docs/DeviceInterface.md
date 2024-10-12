# NetBoxApi.DeviceInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**connectedEndpoint** | **{String: String}** |  Return the appropriate serializer for the type of connected object.  | [optional] [readonly] 
**connectedEndpointType** | **String** |  | [optional] [readonly] 
**connectionStatus** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**countIpaddresses** | **Number** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**enabled** | **Boolean** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lag** | [**NestedInterface**](NestedInterface.md) |  | [optional] 
**macAddress** | **String** |  | [optional] 
**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management | [optional] 
**mode** | [**Mode**](Mode.md) |  | [optional] 
**mtu** | **Number** |  | [optional] 
**name** | **String** |  | 
**taggedVlans** | [**[NestedVLAN]**](NestedVLAN.md) |  | [optional] 
**tags** | **[String]** |  | [optional] 
**type** | [**Type1**](Type1.md) |  | 
**untaggedVlan** | [**NestedVLAN**](NestedVLAN.md) |  | [optional] 


