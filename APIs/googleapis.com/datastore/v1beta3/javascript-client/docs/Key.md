# CloudDatastoreApi.Key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitionId** | [**PartitionId**](PartitionId.md) |  | [optional] 
**path** | [**[PathElement]**](PathElement.md) | The entity path. An entity path consists of one or more elements composed of a kind and a string or numerical identifier, which identify entities. The first element identifies a _root entity_, the second element identifies a _child_ of the root entity, the third element identifies a child of the second entity, and so forth. The entities identified by all prefixes of the path are called the element&#39;s _ancestors_. An entity path is always fully complete: *all* of the entity&#39;s ancestors are required to be in the path along with the entity identifier itself. The only exception is that in some documented cases, the identifier in the last path element (for the entity) itself may be omitted. For example, the last path element of the key of &#x60;Mutation.insert&#x60; may have no identifier. A path can never be empty, and a path can have at most 100 elements. | [optional] 


