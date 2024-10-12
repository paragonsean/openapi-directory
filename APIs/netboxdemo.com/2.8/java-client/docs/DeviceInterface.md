

# DeviceInterface


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**connectedEndpoint** | **Map&lt;String, String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointType** | **String** |  |  [optional] [readonly] |
|**connectionStatus** | [**ConnectionStatus**](ConnectionStatus.md) |  |  [optional] |
|**countIpaddresses** | **Integer** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**device** | [**NestedDevice**](NestedDevice.md) |  |  |
|**enabled** | **Boolean** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lag** | [**NestedInterface**](NestedInterface.md) |  |  [optional] |
|**macAddress** | **String** |  |  [optional] |
|**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management |  [optional] |
|**mode** | [**Mode**](Mode.md) |  |  [optional] |
|**mtu** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**taggedVlans** | [**Set&lt;NestedVLAN&gt;**](NestedVLAN.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**type** | [**Type1**](Type1.md) |  |  |
|**untaggedVlan** | [**NestedVLAN**](NestedVLAN.md) |  |  [optional] |



