# VMwareEngineApi.PeeringRoute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destRange** | **String** | Output only. Destination range of the peering route in CIDR notation. | [optional] [readonly] 
**direction** | **String** | Output only. Direction of the routes exchanged with the peer network, from the VMware Engine network perspective: * Routes of direction &#x60;INCOMING&#x60; are imported from the peer network. * Routes of direction &#x60;OUTGOING&#x60; are exported from the intranet VPC network of the VMware Engine network. | [optional] [readonly] 
**imported** | **Boolean** | Output only. True if the peering route has been imported from a peered VPC network; false otherwise. The import happens if the field &#x60;NetworkPeering.importCustomRoutes&#x60; is true for this network, &#x60;NetworkPeering.exportCustomRoutes&#x60; is true for the peer VPC network, and the import does not result in a route conflict. | [optional] [readonly] 
**nextHopRegion** | **String** | Output only. Region containing the next hop of the peering route. This field only applies to dynamic routes in the peer VPC network. | [optional] [readonly] 
**priority** | **String** | Output only. The priority of the peering route. | [optional] [readonly] 
**type** | **String** | Output only. Type of the route in the peer VPC network. | [optional] [readonly] 



## Enum: DirectionEnum


* `DIRECTION_UNSPECIFIED` (value: `"DIRECTION_UNSPECIFIED"`)

* `INCOMING` (value: `"INCOMING"`)

* `OUTGOING` (value: `"OUTGOING"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `DYNAMIC_PEERING_ROUTE` (value: `"DYNAMIC_PEERING_ROUTE"`)

* `STATIC_PEERING_ROUTE` (value: `"STATIC_PEERING_ROUTE"`)

* `SUBNET_PEERING_ROUTE` (value: `"SUBNET_PEERING_ROUTE"`)




