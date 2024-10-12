# NetBoxApi.PowerFeed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occupied** | **Boolean** |  | [optional] [readonly] 
**amperage** | **Number** |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**cableEnd** | **String** |  | [optional] [readonly] 
**comments** | **String** |  | [optional] 
**connectedEndpoints** | **[String]** |  Return the appropriate serializer for the type of connected object.  | [optional] [readonly] 
**connectedEndpointsReachable** | **Boolean** |  | [optional] [readonly] 
**connectedEndpointsType** | **String** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**linkPeers** | **[String]** |  Return the appropriate serializer for the link termination model.  | [optional] [readonly] 
**linkPeersType** | **String** |  | [optional] [readonly] 
**markConnected** | **Boolean** | Treat as if a cable is connected | [optional] 
**maxUtilization** | **Number** | Maximum permissible draw (percentage) | [optional] 
**name** | **String** |  | 
**phase** | [**Phase**](Phase.md) |  | [optional] 
**powerPanel** | [**NestedPowerPanel**](NestedPowerPanel.md) |  | 
**rack** | [**NestedRack**](NestedRack.md) |  | [optional] 
**status** | [**Status9**](Status9.md) |  | [optional] 
**supply** | [**Supply**](Supply.md) |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**type** | [**Type5**](Type5.md) |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**voltage** | **Number** |  | [optional] 


