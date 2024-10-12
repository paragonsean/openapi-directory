

# PowerFeed


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occupied** | **Boolean** |  |  [optional] [readonly] |
|**amperage** | **Integer** |  |  [optional] |
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**cableEnd** | **String** |  |  [optional] [readonly] |
|**comments** | **String** |  |  [optional] |
|**connectedEndpoints** | **List&lt;String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointsReachable** | **Boolean** |  |  [optional] [readonly] |
|**connectedEndpointsType** | **String** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**linkPeers** | **List&lt;String&gt;** |  Return the appropriate serializer for the link termination model.  |  [optional] [readonly] |
|**linkPeersType** | **String** |  |  [optional] [readonly] |
|**markConnected** | **Boolean** | Treat as if a cable is connected |  [optional] |
|**maxUtilization** | **Integer** | Maximum permissible draw (percentage) |  [optional] |
|**name** | **String** |  |  |
|**phase** | [**Phase**](Phase.md) |  |  [optional] |
|**powerPanel** | [**NestedPowerPanel**](NestedPowerPanel.md) |  |  |
|**rack** | [**NestedRack**](NestedRack.md) |  |  [optional] |
|**status** | [**Status9**](Status9.md) |  |  [optional] |
|**supply** | [**Supply**](Supply.md) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**type** | [**Type5**](Type5.md) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**voltage** | **Integer** |  |  [optional] |



