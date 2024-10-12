

# QueryRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | **Map&lt;String, Object&gt;** | If this parameter is present, the operation only affects vectors that satisfy the filter. See https://www.pinecone.io/docs/metadata-filtering/. |  [optional] |
|**id** | **String** | The unique ID of a vector |  [optional] |
|**includeMetadata** | **Boolean** |  |  [optional] |
|**includeValues** | **Boolean** |  |  [optional] |
|**namespace** | **String** | An index namespace name |  [optional] |
|**sparseVector** | [**SparseVectorData**](SparseVectorData.md) |  |  [optional] |
|**topK** | **Long** | The number of results to return for each query. |  |
|**vector** | **List&lt;Float&gt;** | Vector dense data. This should be the same length as the dimension of the index being queried. |  [optional] |



