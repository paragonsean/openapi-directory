# NetBoxApi.ConsolePort

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occupied** | **Boolean** |  | [optional] [readonly] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**cableEnd** | **String** |  | [optional] [readonly] 
**connectedEndpoints** | **[String]** |  Return the appropriate serializer for the type of connected object.  | [optional] [readonly] 
**connectedEndpointsReachable** | **Boolean** |  | [optional] [readonly] 
**connectedEndpointsType** | **String** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**label** | **String** | Physical label | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**linkPeers** | **[String]** |  Return the appropriate serializer for the link termination model.  | [optional] [readonly] 
**linkPeersType** | **String** |  | [optional] [readonly] 
**markConnected** | **Boolean** | Treat as if a cable is connected | [optional] 
**module** | [**ComponentNestedModule**](ComponentNestedModule.md) |  | [optional] 
**name** | **String** |  | 
**speed** | [**Speed**](Speed.md) |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**type** | [**Type**](Type.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 


