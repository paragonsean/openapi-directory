

# SpokeTypeCount

The number of spokes of a given type that are associated with a specific hub. The type indicates what kind of resource is associated with the spoke.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **String** | Output only. The total number of spokes of this type that are associated with the hub. |  [optional] [readonly] |
|**spokeType** | [**SpokeTypeEnum**](#SpokeTypeEnum) | Output only. The type of the spokes. |  [optional] [readonly] |



## Enum: SpokeTypeEnum

| Name | Value |
|---- | -----|
| SPOKE_TYPE_UNSPECIFIED | &quot;SPOKE_TYPE_UNSPECIFIED&quot; |
| VPN_TUNNEL | &quot;VPN_TUNNEL&quot; |
| INTERCONNECT_ATTACHMENT | &quot;INTERCONNECT_ATTACHMENT&quot; |
| ROUTER_APPLIANCE | &quot;ROUTER_APPLIANCE&quot; |
| VPC_NETWORK | &quot;VPC_NETWORK&quot; |



