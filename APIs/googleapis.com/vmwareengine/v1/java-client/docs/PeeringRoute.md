

# PeeringRoute

Exchanged network peering route.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destRange** | **String** | Output only. Destination range of the peering route in CIDR notation. |  [optional] [readonly] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | Output only. Direction of the routes exchanged with the peer network, from the VMware Engine network perspective: * Routes of direction &#x60;INCOMING&#x60; are imported from the peer network. * Routes of direction &#x60;OUTGOING&#x60; are exported from the intranet VPC network of the VMware Engine network. |  [optional] [readonly] |
|**imported** | **Boolean** | Output only. True if the peering route has been imported from a peered VPC network; false otherwise. The import happens if the field &#x60;NetworkPeering.importCustomRoutes&#x60; is true for this network, &#x60;NetworkPeering.exportCustomRoutes&#x60; is true for the peer VPC network, and the import does not result in a route conflict. |  [optional] [readonly] |
|**nextHopRegion** | **String** | Output only. Region containing the next hop of the peering route. This field only applies to dynamic routes in the peer VPC network. |  [optional] [readonly] |
|**priority** | **String** | Output only. The priority of the peering route. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Type of the route in the peer VPC network. |  [optional] [readonly] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| DIRECTION_UNSPECIFIED | &quot;DIRECTION_UNSPECIFIED&quot; |
| INCOMING | &quot;INCOMING&quot; |
| OUTGOING | &quot;OUTGOING&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| DYNAMIC_PEERING_ROUTE | &quot;DYNAMIC_PEERING_ROUTE&quot; |
| STATIC_PEERING_ROUTE | &quot;STATIC_PEERING_ROUTE&quot; |
| SUBNET_PEERING_ROUTE | &quot;SUBNET_PEERING_ROUTE&quot; |



