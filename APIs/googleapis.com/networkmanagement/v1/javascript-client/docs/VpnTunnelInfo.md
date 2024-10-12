# NetworkManagementApi.VpnTunnelInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Name of a VPN tunnel. | [optional] 
**networkUri** | **String** | URI of a Compute Engine network where the VPN tunnel is configured. | [optional] 
**region** | **String** | Name of a Google Cloud region where this VPN tunnel is configured. | [optional] 
**remoteGateway** | **String** | URI of a VPN gateway at remote end of the tunnel. | [optional] 
**remoteGatewayIp** | **String** | Remote VPN gateway&#39;s IP address. | [optional] 
**routingType** | **String** | Type of the routing policy. | [optional] 
**sourceGateway** | **String** | URI of the VPN gateway at local end of the tunnel. | [optional] 
**sourceGatewayIp** | **String** | Local VPN gateway&#39;s IP address. | [optional] 
**uri** | **String** | URI of a VPN tunnel. | [optional] 



## Enum: RoutingTypeEnum


* `ROUTING_TYPE_UNSPECIFIED` (value: `"ROUTING_TYPE_UNSPECIFIED"`)

* `ROUTE_BASED` (value: `"ROUTE_BASED"`)

* `POLICY_BASED` (value: `"POLICY_BASED"`)

* `DYNAMIC` (value: `"DYNAMIC"`)




