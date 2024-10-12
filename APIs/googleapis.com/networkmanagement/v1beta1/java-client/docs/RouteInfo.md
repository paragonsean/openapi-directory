

# RouteInfo

For display only. Metadata associated with a Compute Engine route.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destIpRange** | **String** | Destination IP range of the route. |  [optional] |
|**destPortRanges** | **List&lt;String&gt;** | Destination port ranges of the route. Policy based routes only. |  [optional] |
|**displayName** | **String** | Name of a route. |  [optional] |
|**instanceTags** | **List&lt;String&gt;** | Instance tags of the route. |  [optional] |
|**nccHubUri** | **String** | URI of a NCC Hub. NCC_HUB routes only. |  [optional] |
|**nccSpokeUri** | **String** | URI of a NCC Spoke. NCC_HUB routes only. |  [optional] |
|**networkUri** | **String** | URI of a Compute Engine network. NETWORK routes only. |  [optional] |
|**nextHop** | **String** | Next hop of the route. |  [optional] |
|**nextHopType** | [**NextHopTypeEnum**](#NextHopTypeEnum) | Type of next hop. |  [optional] |
|**priority** | **Integer** | Priority of the route. |  [optional] |
|**protocols** | **List&lt;String&gt;** | Protocols of the route. Policy based routes only. |  [optional] |
|**routeScope** | [**RouteScopeEnum**](#RouteScopeEnum) | Indicates where route is applicable. |  [optional] |
|**routeType** | [**RouteTypeEnum**](#RouteTypeEnum) | Type of route. |  [optional] |
|**srcIpRange** | **String** | Source IP address range of the route. Policy based routes only. |  [optional] |
|**srcPortRanges** | **List&lt;String&gt;** | Source port ranges of the route. Policy based routes only. |  [optional] |
|**uri** | **String** | URI of a route. Dynamic, peering static and peering dynamic routes do not have an URI. Advertised route from Google Cloud VPC to on-premises network also does not have an URI. |  [optional] |



## Enum: NextHopTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;NEXT_HOP_TYPE_UNSPECIFIED&quot; |
| IP | &quot;NEXT_HOP_IP&quot; |
| INSTANCE | &quot;NEXT_HOP_INSTANCE&quot; |
| NETWORK | &quot;NEXT_HOP_NETWORK&quot; |
| PEERING | &quot;NEXT_HOP_PEERING&quot; |
| INTERCONNECT | &quot;NEXT_HOP_INTERCONNECT&quot; |
| VPN_TUNNEL | &quot;NEXT_HOP_VPN_TUNNEL&quot; |
| VPN_GATEWAY | &quot;NEXT_HOP_VPN_GATEWAY&quot; |
| INTERNET_GATEWAY | &quot;NEXT_HOP_INTERNET_GATEWAY&quot; |
| BLACKHOLE | &quot;NEXT_HOP_BLACKHOLE&quot; |
| ILB | &quot;NEXT_HOP_ILB&quot; |
| ROUTER_APPLIANCE | &quot;NEXT_HOP_ROUTER_APPLIANCE&quot; |
| NCC_HUB | &quot;NEXT_HOP_NCC_HUB&quot; |



## Enum: RouteScopeEnum

| Name | Value |
|---- | -----|
| ROUTE_SCOPE_UNSPECIFIED | &quot;ROUTE_SCOPE_UNSPECIFIED&quot; |
| NETWORK | &quot;NETWORK&quot; |
| NCC_HUB | &quot;NCC_HUB&quot; |



## Enum: RouteTypeEnum

| Name | Value |
|---- | -----|
| ROUTE_TYPE_UNSPECIFIED | &quot;ROUTE_TYPE_UNSPECIFIED&quot; |
| SUBNET | &quot;SUBNET&quot; |
| STATIC | &quot;STATIC&quot; |
| DYNAMIC | &quot;DYNAMIC&quot; |
| PEERING_SUBNET | &quot;PEERING_SUBNET&quot; |
| PEERING_STATIC | &quot;PEERING_STATIC&quot; |
| PEERING_DYNAMIC | &quot;PEERING_DYNAMIC&quot; |
| POLICY_BASED | &quot;POLICY_BASED&quot; |



