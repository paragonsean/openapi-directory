

# InvocationConfig

Includes various configuration options for a workflow invocation. If both `included_targets` and `included_tags` are unset, all actions will be included.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fullyRefreshIncrementalTablesEnabled** | **Boolean** | Optional. When set to true, any incremental tables will be fully refreshed. |  [optional] |
|**includedTags** | **List&lt;String&gt;** | Optional. The set of tags to include. |  [optional] |
|**includedTargets** | [**List&lt;Target&gt;**](Target.md) | Optional. The set of action identifiers to include. |  [optional] |
|**serviceAccount** | **String** | Optional. The service account to run workflow invocations under. |  [optional] |
|**transitiveDependenciesIncluded** | **Boolean** | Optional. When set to true, transitive dependencies of included actions will be executed. |  [optional] |
|**transitiveDependentsIncluded** | **Boolean** | Optional. When set to true, transitive dependents of included actions will be executed. |  [optional] |



