

# ModelInterface


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**circuitTermination** | [**InterfaceCircuitTermination**](InterfaceCircuitTermination.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | [**NestedDevice**](NestedDevice.md) |  |  |
|**enabled** | **Boolean** |  |  [optional] |
|**formFactor** | [**FormFactor**](FormFactor.md) |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**interfaceConnection** | **String** |  |  [optional] [readonly] |
|**isConnected** | **String** |  |  [optional] [readonly] |
|**lag** | [**NestedInterface**](NestedInterface.md) |  |  [optional] |
|**macAddress** | **String** |  |  [optional] |
|**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management |  [optional] |
|**mode** | [**Mode**](Mode.md) |  |  [optional] |
|**mtu** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**taggedVlans** | [**Set&lt;InterfaceVLAN&gt;**](InterfaceVLAN.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**untaggedVlan** | [**InterfaceVLAN**](InterfaceVLAN.md) |  |  [optional] |



