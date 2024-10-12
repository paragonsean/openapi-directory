# NetBoxApi.WritablePowerFeed

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
**phase** | **String** |  | [optional] 
**powerPanel** | **Number** |  | 
**rack** | **Number** |  | [optional] 
**status** | **String** |  | [optional] 
**supply** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**type** | **String** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**voltage** | **Number** |  | [optional] 



## Enum: PhaseEnum


* `single-phase` (value: `"single-phase"`)

* `three-phase` (value: `"three-phase"`)





## Enum: StatusEnum


* `offline` (value: `"offline"`)

* `active` (value: `"active"`)

* `planned` (value: `"planned"`)

* `failed` (value: `"failed"`)





## Enum: SupplyEnum


* `ac` (value: `"ac"`)

* `dc` (value: `"dc"`)





## Enum: TypeEnum


* `primary` (value: `"primary"`)

* `redundant` (value: `"redundant"`)




