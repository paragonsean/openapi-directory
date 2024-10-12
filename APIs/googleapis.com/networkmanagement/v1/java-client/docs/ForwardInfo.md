

# ForwardInfo

Details of the final state \"forward\" and associated resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipAddress** | **String** | IP address of the target (if applicable). |  [optional] |
|**resourceUri** | **String** | URI of the resource that the packet is forwarded to. |  [optional] |
|**target** | [**TargetEnum**](#TargetEnum) | Target type where this packet is forwarded to. |  [optional] |



## Enum: TargetEnum

| Name | Value |
|---- | -----|
| TARGET_UNSPECIFIED | &quot;TARGET_UNSPECIFIED&quot; |
| PEERING_VPC | &quot;PEERING_VPC&quot; |
| VPN_GATEWAY | &quot;VPN_GATEWAY&quot; |
| INTERCONNECT | &quot;INTERCONNECT&quot; |
| GKE_MASTER | &quot;GKE_MASTER&quot; |
| IMPORTED_CUSTOM_ROUTE_NEXT_HOP | &quot;IMPORTED_CUSTOM_ROUTE_NEXT_HOP&quot; |
| CLOUD_SQL_INSTANCE | &quot;CLOUD_SQL_INSTANCE&quot; |
| ANOTHER_PROJECT | &quot;ANOTHER_PROJECT&quot; |
| NCC_HUB | &quot;NCC_HUB&quot; |
| ROUTER_APPLIANCE | &quot;ROUTER_APPLIANCE&quot; |



