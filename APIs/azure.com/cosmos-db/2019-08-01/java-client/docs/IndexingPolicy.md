

# IndexingPolicy

Cosmos DB indexing policy

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automatic** | **Boolean** | Indicates if the indexing policy is automatic |  [optional] |
|**compositeIndexes** | **List&lt;List&lt;CompositePath&gt;&gt;** | List of composite path list |  [optional] |
|**excludedPaths** | [**List&lt;ExcludedPath&gt;**](ExcludedPath.md) | List of paths to exclude from indexing |  [optional] |
|**includedPaths** | [**List&lt;IncludedPath&gt;**](IncludedPath.md) | List of paths to include in the indexing |  [optional] |
|**indexingMode** | [**IndexingModeEnum**](#IndexingModeEnum) | Indicates the indexing mode. |  [optional] |
|**spatialIndexes** | [**List&lt;SpatialSpec&gt;**](SpatialSpec.md) | List of spatial specifics |  [optional] |



## Enum: IndexingModeEnum

| Name | Value |
|---- | -----|
| CONSISTENT | &quot;Consistent&quot; |
| LAZY | &quot;Lazy&quot; |
| NONE | &quot;None&quot; |



