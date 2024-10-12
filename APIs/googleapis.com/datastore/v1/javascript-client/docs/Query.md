# CloudDatastoreApi.Query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinctOn** | [**[PropertyReference]**](PropertyReference.md) | The properties to make distinct. The query results will contain the first result for each distinct combination of values for the given properties (if empty, all results are returned). Requires: * If &#x60;order&#x60; is specified, the set of distinct on properties must appear before the non-distinct on properties in &#x60;order&#x60;. | [optional] 
**endCursor** | **Blob** | An ending point for the query results. Query cursors are returned in query result batches and [can only be used to limit the same query](https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets). | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**kind** | [**[KindExpression]**](KindExpression.md) | The kinds to query (if empty, returns entities of all kinds). Currently at most 1 kind may be specified. | [optional] 
**limit** | **Number** | The maximum number of results to return. Applies after all other constraints. Optional. Unspecified is interpreted as no limit. Must be &gt;&#x3D; 0 if specified. | [optional] 
**offset** | **Number** | The number of results to skip. Applies before limit, but after all other constraints. Optional. Must be &gt;&#x3D; 0 if specified. | [optional] 
**order** | [**[PropertyOrder]**](PropertyOrder.md) | The order to apply to the query results (if empty, order is unspecified). | [optional] 
**projection** | [**[Projection]**](Projection.md) | The projection to return. Defaults to returning all properties. | [optional] 
**startCursor** | **Blob** | A starting point for the query results. Query cursors are returned in query result batches and [can only be used to continue the same query](https://cloud.google.com/datastore/docs/concepts/queries#cursors_limits_and_offsets). | [optional] 


