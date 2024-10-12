# NetworkManagementApi.ForwardInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipAddress** | **String** | IP address of the target (if applicable). | [optional] 
**resourceUri** | **String** | URI of the resource that the packet is forwarded to. | [optional] 
**target** | **String** | Target type where this packet is forwarded to. | [optional] 



## Enum: TargetEnum


* `TARGET_UNSPECIFIED` (value: `"TARGET_UNSPECIFIED"`)

* `PEERING_VPC` (value: `"PEERING_VPC"`)

* `VPN_GATEWAY` (value: `"VPN_GATEWAY"`)

* `INTERCONNECT` (value: `"INTERCONNECT"`)

* `GKE_MASTER` (value: `"GKE_MASTER"`)

* `IMPORTED_CUSTOM_ROUTE_NEXT_HOP` (value: `"IMPORTED_CUSTOM_ROUTE_NEXT_HOP"`)

* `CLOUD_SQL_INSTANCE` (value: `"CLOUD_SQL_INSTANCE"`)

* `ANOTHER_PROJECT` (value: `"ANOTHER_PROJECT"`)

* `NCC_HUB` (value: `"NCC_HUB"`)

* `ROUTER_APPLIANCE` (value: `"ROUTER_APPLIANCE"`)




