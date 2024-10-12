# NetworkManagementClient.NextHopResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextHopIpAddress** | **String** | Next hop IP Address | [optional] 
**nextHopType** | **String** | Next hop type. | [optional] 
**routeTableId** | **String** | The resource identifier for the route table associated with the route being returned. If the route being returned does not correspond to any user created routes then this field will be the string &#39;System Route&#39;. | [optional] 



## Enum: NextHopTypeEnum


* `Internet` (value: `"Internet"`)

* `VirtualAppliance` (value: `"VirtualAppliance"`)

* `VirtualNetworkGateway` (value: `"VirtualNetworkGateway"`)

* `VnetLocal` (value: `"VnetLocal"`)

* `HyperNetGateway` (value: `"HyperNetGateway"`)

* `None` (value: `"None"`)




