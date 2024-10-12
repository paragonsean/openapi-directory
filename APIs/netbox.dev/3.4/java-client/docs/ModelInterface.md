

# ModelInterface


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occupied** | **Boolean** |  |  [optional] [readonly] |
|**bridge** | [**NestedInterface**](NestedInterface.md) |  |  [optional] |
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**cableEnd** | **String** |  |  [optional] [readonly] |
|**connectedEndpoints** | **List&lt;String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointsReachable** | **Boolean** |  |  [optional] [readonly] |
|**connectedEndpointsType** | **String** |  |  [optional] [readonly] |
|**countFhrpGroups** | **Integer** |  |  [optional] [readonly] |
|**countIpaddresses** | **Integer** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | [**NestedDevice**](NestedDevice.md) |  |  |
|**display** | **String** |  |  [optional] [readonly] |
|**duplex** | [**Duplex**](Duplex.md) |  |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**l2vpnTermination** | [**NestedL2VPNTermination**](NestedL2VPNTermination.md) |  |  [optional] |
|**label** | **String** | Physical label |  [optional] |
|**lag** | [**NestedInterface**](NestedInterface.md) |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**linkPeers** | **List&lt;String&gt;** |  Return the appropriate serializer for the link termination model.  |  [optional] [readonly] |
|**linkPeersType** | **String** |  |  [optional] [readonly] |
|**macAddress** | **String** |  |  [optional] |
|**markConnected** | **Boolean** | Treat as if a cable is connected |  [optional] |
|**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management |  [optional] |
|**mode** | [**Mode**](Mode.md) |  |  [optional] |
|**module** | [**ComponentNestedModule**](ComponentNestedModule.md) |  |  [optional] |
|**mtu** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**parent** | [**NestedInterface**](NestedInterface.md) |  |  [optional] |
|**poeMode** | [**PoeMode**](PoeMode.md) |  |  [optional] |
|**poeType** | [**PoeType**](PoeType.md) |  |  [optional] |
|**rfChannel** | [**RfChannel**](RfChannel.md) |  |  [optional] |
|**rfChannelFrequency** | **BigDecimal** |  |  [optional] |
|**rfChannelWidth** | **BigDecimal** |  |  [optional] |
|**rfRole** | [**RfRole**](RfRole.md) |  |  [optional] |
|**speed** | **Integer** |  |  [optional] |
|**taggedVlans** | [**Set&lt;NestedVLAN&gt;**](NestedVLAN.md) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**txPower** | **Integer** |  |  [optional] |
|**type** | [**Type3**](Type3.md) |  |  |
|**untaggedVlan** | [**NestedVLAN**](NestedVLAN.md) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vdcs** | [**Set&lt;NestedVirtualDeviceContext&gt;**](NestedVirtualDeviceContext.md) |  |  [optional] |
|**vrf** | [**NestedVRF**](NestedVRF.md) |  |  [optional] |
|**wirelessLans** | [**Set&lt;NestedWirelessLAN&gt;**](NestedWirelessLAN.md) |  |  [optional] |
|**wirelessLink** | [**NestedWirelessLink**](NestedWirelessLink.md) |  |  [optional] |
|**wwn** | **String** | 64-bit World Wide Name |  [optional] |



