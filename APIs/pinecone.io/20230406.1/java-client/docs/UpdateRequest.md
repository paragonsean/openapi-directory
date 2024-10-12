

# UpdateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The vector&#39;s unique ID |  |
|**namespace** | **String** | An index namespace name |  [optional] |
|**setMetadata** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**sparseValues** | [**SparseVectorData**](SparseVectorData.md) |  |  [optional] |
|**values** | **List&lt;Float&gt;** | Vector dense data. This should be the same length as the dimension of the index being queried. |  [optional] |



