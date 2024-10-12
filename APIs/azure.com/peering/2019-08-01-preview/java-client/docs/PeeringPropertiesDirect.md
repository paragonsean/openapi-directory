

# PeeringPropertiesDirect

The properties that define a direct peering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connections** | [**List&lt;DirectConnection&gt;**](DirectConnection.md) | The set of connections that constitute a direct peering. |  [optional] |
|**directPeeringType** | [**DirectPeeringTypeEnum**](#DirectPeeringTypeEnum) | The type of direct peering. |  [optional] |
|**peerAsn** | [**SubResource**](SubResource.md) |  |  [optional] |
|**useForPeeringService** | **Boolean** | The flag that indicates whether or not the peering is used for peering service. |  [optional] |



## Enum: DirectPeeringTypeEnum

| Name | Value |
|---- | -----|
| EDGE | &quot;Edge&quot; |
| TRANSIT | &quot;Transit&quot; |
| CDN | &quot;Cdn&quot; |
| INTERNAL | &quot;Internal&quot; |



