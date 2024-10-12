# NetBoxApi.CircuitTermination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occupied** | **Boolean** |  | [optional] [readonly] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**cableEnd** | **String** |  | [optional] [readonly] 
**circuit** | [**NestedCircuit**](NestedCircuit.md) |  | 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**linkPeers** | **[String]** |  Return the appropriate serializer for the link termination model.  | [optional] [readonly] 
**linkPeersType** | **String** |  | [optional] [readonly] 
**markConnected** | **Boolean** | Treat as if a cable is connected | [optional] 
**portSpeed** | **Number** |  | [optional] 
**ppInfo** | **String** |  | [optional] 
**providerNetwork** | [**NestedProviderNetwork**](NestedProviderNetwork.md) |  | [optional] 
**site** | [**NestedSite**](NestedSite.md) |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**termSide** | **String** |  | 
**upstreamSpeed** | **Number** | Upstream speed, if different from port speed | [optional] 
**url** | **String** |  | [optional] [readonly] 
**xconnectId** | **String** |  | [optional] 



## Enum: TermSideEnum


* `A` (value: `"A"`)

* `Z` (value: `"Z"`)




