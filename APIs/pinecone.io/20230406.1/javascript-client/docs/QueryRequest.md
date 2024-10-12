# PineconeApi.QueryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **{String: Object}** | If this parameter is present, the operation only affects vectors that satisfy the filter. See https://www.pinecone.io/docs/metadata-filtering/. | [optional] 
**id** | **String** | The unique ID of a vector | [optional] 
**includeMetadata** | **Boolean** |  | [optional] [default to false]
**includeValues** | **Boolean** |  | [optional] [default to false]
**namespace** | **String** | An index namespace name | [optional] 
**sparseVector** | [**SparseVectorData**](SparseVectorData.md) |  | [optional] 
**topK** | **Number** | The number of results to return for each query. | [default to 100]
**vector** | **[Number]** | Vector dense data. This should be the same length as the dimension of the index being queried. | [optional] 


