# VoodooManufacturing3DPrintApi.Material

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **String** | Name for the color of this material. This field is for display only and is not required for creating an order (use the material&#39;s id). | [optional] 
**colorSample** | **String** | A hex value providing an approximate visual sample of this color. | [optional] 
**id** | **Number** | The unique identifier for this material. Use this value when submitting order items to specify that an ordered model should be printed with a specific material. | [optional] 
**type** | **String** | Type of material, excluding color. Will be one of \&quot;PLA\&quot;, \&quot;Semi-flex TPU\&quot;, or \&quot;Full-flex TPU\&quot;. This field is for display only and is not required for creating an order (use the material&#39;s id). | [optional] 


