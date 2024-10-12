# VoodooManufacturing3DPrintApi.Print

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**materialId** | **Number** | The unique identifier of the material you&#39;d like to print in. This value comes from the id field of the material object. | [optional] 
**modelId** | **Number** | The unique identifier of the model you&#39;d like to print. This value comes from the id field of the model object. | [optional] 
**options** | [**ProductionOptions**](ProductionOptions.md) |  | [optional] 
**quantity** | **Number** | The number of prints to order for this material/model pair. | [optional] 
**units** | **String** | The units of the model file. Either \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. The correct value to pass here depends on which design program you&#39;re using. Defaults to \&quot;mm\&quot;. | [optional] 


