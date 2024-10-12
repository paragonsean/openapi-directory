# PeeringManagementClient.PeeringPropertiesDirect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**[DirectConnection]**](DirectConnection.md) | The set of connections that constitute a direct peering. | [optional] 
**directPeeringType** | **String** | The type of direct peering. | [optional] 
**peerAsn** | [**SubResource**](SubResource.md) |  | [optional] 
**useForPeeringService** | **Boolean** | The flag that indicates whether or not the peering is used for peering service. | [optional] 



## Enum: DirectPeeringTypeEnum


* `Edge` (value: `"Edge"`)

* `Transit` (value: `"Transit"`)

* `Cdn` (value: `"Cdn"`)

* `Internal` (value: `"Internal"`)




