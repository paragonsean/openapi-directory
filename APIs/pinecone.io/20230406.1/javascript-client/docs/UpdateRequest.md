# PineconeApi.UpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The vector&#39;s unique ID | 
**namespace** | **String** | An index namespace name | [optional] 
**setMetadata** | **{String: Object}** |  | [optional] 
**sparseValues** | [**SparseVectorData**](SparseVectorData.md) |  | [optional] 
**values** | **[Number]** | Vector dense data. This should be the same length as the dimension of the index being queried. | [optional] 


