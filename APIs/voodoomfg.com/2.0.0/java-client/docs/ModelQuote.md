

# ModelQuote

Quote for a model in the given material_id, units, and quantity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**materialId** | **Integer** | Requested material id. |  [optional] |
|**modelId** | **Integer** | Requested model id. Not present on the response from /model/quote_attrs. |  [optional] |
|**options** | [**ProductionOptionsCosts**](ProductionOptionsCosts.md) |  |  [optional] |
|**quote** | **BigDecimal** | The cost for printing the model in the requested quantity, before any additional services. |  [optional] |
|**unitCost** | **BigDecimal** | The cost of a single print of the specified model. |  [optional] |
|**units** | **String** | Units for the requested print. One of \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. |  [optional] |



