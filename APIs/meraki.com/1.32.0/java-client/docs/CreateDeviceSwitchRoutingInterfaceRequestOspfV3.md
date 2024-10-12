

# CreateDeviceSwitchRoutingInterfaceRequestOspfV3

The OSPFv3 routing settings of the interface.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**area** | **String** | The OSPFv3 area to which this interface should belong. Can be either &#39;disabled&#39; or the identifier of an           existing OSPFv3 area. Defaults to &#39;disabled&#39;. |  [optional] |
|**cost** | **Integer** | The path cost for this interface. Defaults to 1, but can be increased up to 65535           to give lower priority. |  [optional] |
|**isPassiveEnabled** | **Boolean** | When enabled, OSPFv3 will not run on the interface, but the subnet will still be advertised. |  [optional] |



