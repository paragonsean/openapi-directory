# CosmosDb.IndexingPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic** | **Boolean** | Indicates if the indexing policy is automatic | [optional] 
**excludedPaths** | [**[ExcludedPath]**](ExcludedPath.md) | List of paths to exclude from indexing | [optional] 
**includedPaths** | [**[IncludedPath]**](IncludedPath.md) | List of paths to include in the indexing | [optional] 
**indexingMode** | **String** | Indicates the indexing mode. | [optional] [default to &#39;Consistent&#39;]



## Enum: IndexingModeEnum


* `Consistent` (value: `"Consistent"`)

* `Lazy` (value: `"Lazy"`)

* `None` (value: `"None"`)




