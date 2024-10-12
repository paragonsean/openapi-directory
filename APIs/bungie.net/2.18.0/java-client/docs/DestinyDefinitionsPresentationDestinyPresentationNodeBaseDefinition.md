

# DestinyDefinitionsPresentationDestinyPresentationNodeBaseDefinition

This is the base class for all presentation system children. Presentation Nodes, Records, Collectibles, and Metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hash** | **Integer** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. |  [optional] |
|**index** | **Integer** | The index of the entity as it was found in the investment tables. |  [optional] |
|**parentNodeHashes** | **List&lt;Integer&gt;** | A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents. |  [optional] |
|**presentationNodeType** | **Integer** |  |  [optional] |
|**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! |  [optional] |
|**traitHashes** | **List&lt;Integer&gt;** |  |  [optional] |
|**traitIds** | **List&lt;String&gt;** |  |  [optional] |



