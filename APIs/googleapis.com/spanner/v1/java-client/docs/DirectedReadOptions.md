

# DirectedReadOptions

The DirectedReadOptions can be used to indicate which replicas or regions should be used for non-transactional reads or queries. DirectedReadOptions may only be specified for a read-only transaction, otherwise the API will return an `INVALID_ARGUMENT` error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludeReplicas** | [**ExcludeReplicas**](ExcludeReplicas.md) |  |  [optional] |
|**includeReplicas** | [**IncludeReplicas**](IncludeReplicas.md) |  |  [optional] |



