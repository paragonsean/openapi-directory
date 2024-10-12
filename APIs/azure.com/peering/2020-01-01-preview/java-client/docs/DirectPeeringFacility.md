

# DirectPeeringFacility

The properties that define a direct peering facility.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The address of the direct peering facility. |  [optional] |
|**directPeeringType** | [**DirectPeeringTypeEnum**](#DirectPeeringTypeEnum) | The type of the direct peering. |  [optional] |
|**peeringDBFacilityId** | **Integer** | The PeeringDB.com ID of the facility. |  [optional] |
|**peeringDBFacilityLink** | **String** | The PeeringDB.com URL of the facility. |  [optional] |



## Enum: DirectPeeringTypeEnum

| Name | Value |
|---- | -----|
| EDGE | &quot;Edge&quot; |
| TRANSIT | &quot;Transit&quot; |
| CDN | &quot;Cdn&quot; |
| INTERNAL | &quot;Internal&quot; |
| IX | &quot;Ix&quot; |
| IX_RS | &quot;IxRs&quot; |



