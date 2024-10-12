# VoodooManufacturing3DPrintApi.ModelQuote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**materialId** | **Number** | Requested material id. | [optional] 
**modelId** | **Number** | Requested model id. Not present on the response from /model/quote_attrs. | [optional] 
**options** | [**ProductionOptionsCosts**](ProductionOptionsCosts.md) |  | [optional] 
**quote** | **Number** | The cost for printing the model in the requested quantity, before any additional services. | [optional] 
**unitCost** | **Number** | The cost of a single print of the specified model. | [optional] 
**units** | **String** | Units for the requested print. One of \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. | [optional] 


