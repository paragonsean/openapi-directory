# NetBoxApi.Interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occupied** | **Boolean** |  | [optional] [readonly] 
**bridge** | [**NestedInterface**](NestedInterface.md) |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**cableEnd** | **String** |  | [optional] [readonly] 
**connectedEndpoints** | **[String]** |  Return the appropriate serializer for the type of connected object.  | [optional] [readonly] 
**connectedEndpointsReachable** | **Boolean** |  | [optional] [readonly] 
**connectedEndpointsType** | **String** |  | [optional] [readonly] 
**countFhrpGroups** | **Number** |  | [optional] [readonly] 
**countIpaddresses** | **Number** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**display** | **String** |  | [optional] [readonly] 
**duplex** | [**Duplex**](Duplex.md) |  | [optional] 
**enabled** | **Boolean** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**l2vpnTermination** | [**NestedL2VPNTermination**](NestedL2VPNTermination.md) |  | [optional] 
**label** | **String** | Physical label | [optional] 
**lag** | [**NestedInterface**](NestedInterface.md) |  | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**linkPeers** | **[String]** |  Return the appropriate serializer for the link termination model.  | [optional] [readonly] 
**linkPeersType** | **String** |  | [optional] [readonly] 
**macAddress** | **String** |  | [optional] 
**markConnected** | **Boolean** | Treat as if a cable is connected | [optional] 
**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management | [optional] 
**mode** | [**Mode**](Mode.md) |  | [optional] 
**module** | [**ComponentNestedModule**](ComponentNestedModule.md) |  | [optional] 
**mtu** | **Number** |  | [optional] 
**name** | **String** |  | 
**parent** | [**NestedInterface**](NestedInterface.md) |  | [optional] 
**poeMode** | [**PoeMode**](PoeMode.md) |  | [optional] 
**poeType** | [**PoeType**](PoeType.md) |  | [optional] 
**rfChannel** | [**RfChannel**](RfChannel.md) |  | [optional] 
**rfChannelFrequency** | **Number** |  | [optional] 
**rfChannelWidth** | **Number** |  | [optional] 
**rfRole** | [**RfRole**](RfRole.md) |  | [optional] 
**speed** | **Number** |  | [optional] 
**taggedVlans** | [**[NestedVLAN]**](NestedVLAN.md) |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**txPower** | **Number** |  | [optional] 
**type** | [**Type3**](Type3.md) |  | 
**untaggedVlan** | [**NestedVLAN**](NestedVLAN.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vdcs** | [**[NestedVirtualDeviceContext]**](NestedVirtualDeviceContext.md) |  | [optional] 
**vrf** | [**NestedVRF**](NestedVRF.md) |  | [optional] 
**wirelessLans** | [**[NestedWirelessLAN]**](NestedWirelessLAN.md) |  | [optional] 
**wirelessLink** | [**NestedWirelessLink**](NestedWirelessLink.md) |  | [optional] 
**wwn** | **String** | 64-bit World Wide Name | [optional] 


