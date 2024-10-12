# NetBoxApi.CircuitTermination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**circuit** | [**NestedCircuit**](NestedCircuit.md) |  | 
**connectedEndpoint** | **{String: String}** |  Return the appropriate serializer for the type of connected object.  | [optional] [readonly] 
**connectedEndpointType** | **String** |  | [optional] [readonly] 
**connectionStatus** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**description** | **String** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**portSpeed** | **Number** |  | 
**ppInfo** | **String** |  | [optional] 
**site** | [**NestedSite**](NestedSite.md) |  | 
**termSide** | **String** |  | 
**upstreamSpeed** | **Number** | Upstream speed, if different from port speed | [optional] 
**xconnectId** | **String** |  | [optional] 



## Enum: TermSideEnum


* `A` (value: `"A"`)

* `Z` (value: `"Z"`)




