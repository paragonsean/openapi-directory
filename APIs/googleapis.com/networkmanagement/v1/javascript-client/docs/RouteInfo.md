# NetworkManagementApi.RouteInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destIpRange** | **String** | Destination IP range of the route. | [optional] 
**destPortRanges** | **[String]** | Destination port ranges of the route. Policy based routes only. | [optional] 
**displayName** | **String** | Name of a route. | [optional] 
**instanceTags** | **[String]** | Instance tags of the route. | [optional] 
**nccHubUri** | **String** | URI of a NCC Hub. NCC_HUB routes only. | [optional] 
**nccSpokeUri** | **String** | URI of a NCC Spoke. NCC_HUB routes only. | [optional] 
**networkUri** | **String** | URI of a Compute Engine network. NETWORK routes only. | [optional] 
**nextHop** | **String** | Next hop of the route. | [optional] 
**nextHopType** | **String** | Type of next hop. | [optional] 
**priority** | **Number** | Priority of the route. | [optional] 
**protocols** | **[String]** | Protocols of the route. Policy based routes only. | [optional] 
**routeScope** | **String** | Indicates where route is applicable. | [optional] 
**routeType** | **String** | Type of route. | [optional] 
**srcIpRange** | **String** | Source IP address range of the route. Policy based routes only. | [optional] 
**srcPortRanges** | **[String]** | Source port ranges of the route. Policy based routes only. | [optional] 
**uri** | **String** | URI of a route. Dynamic, peering static and peering dynamic routes do not have an URI. Advertised route from Google Cloud VPC to on-premises network also does not have an URI. | [optional] 



## Enum: NextHopTypeEnum


* `TYPE_UNSPECIFIED` (value: `"NEXT_HOP_TYPE_UNSPECIFIED"`)

* `IP` (value: `"NEXT_HOP_IP"`)

* `INSTANCE` (value: `"NEXT_HOP_INSTANCE"`)

* `NETWORK` (value: `"NEXT_HOP_NETWORK"`)

* `PEERING` (value: `"NEXT_HOP_PEERING"`)

* `INTERCONNECT` (value: `"NEXT_HOP_INTERCONNECT"`)

* `VPN_TUNNEL` (value: `"NEXT_HOP_VPN_TUNNEL"`)

* `VPN_GATEWAY` (value: `"NEXT_HOP_VPN_GATEWAY"`)

* `INTERNET_GATEWAY` (value: `"NEXT_HOP_INTERNET_GATEWAY"`)

* `BLACKHOLE` (value: `"NEXT_HOP_BLACKHOLE"`)

* `ILB` (value: `"NEXT_HOP_ILB"`)

* `ROUTER_APPLIANCE` (value: `"NEXT_HOP_ROUTER_APPLIANCE"`)

* `NCC_HUB` (value: `"NEXT_HOP_NCC_HUB"`)





## Enum: RouteScopeEnum


* `ROUTE_SCOPE_UNSPECIFIED` (value: `"ROUTE_SCOPE_UNSPECIFIED"`)

* `NETWORK` (value: `"NETWORK"`)

* `NCC_HUB` (value: `"NCC_HUB"`)





## Enum: RouteTypeEnum


* `ROUTE_TYPE_UNSPECIFIED` (value: `"ROUTE_TYPE_UNSPECIFIED"`)

* `SUBNET` (value: `"SUBNET"`)

* `STATIC` (value: `"STATIC"`)

* `DYNAMIC` (value: `"DYNAMIC"`)

* `PEERING_SUBNET` (value: `"PEERING_SUBNET"`)

* `PEERING_STATIC` (value: `"PEERING_STATIC"`)

* `PEERING_DYNAMIC` (value: `"PEERING_DYNAMIC"`)

* `POLICY_BASED` (value: `"POLICY_BASED"`)




