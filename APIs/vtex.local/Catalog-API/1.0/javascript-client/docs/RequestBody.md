# CatalogApi.RequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldId** | **Number** | Specification unique identifier. This field cannot be updated. | 
**fieldValueId** | **Number** | Specification value unique identifier. This field can only be updated with other values of the same &#x60;FieldId&#x60;. | 
**id** | **Number** | Specification and SKU association unique identifier. This field cannot be updated. | 
**skuId** | **Number** | SKU unique identifier. This field cannot be updated. | [optional] 
**text** | **String** | Specification Value Name. This field is automatically updated if the &#x60;FieldValue&#x60; is updated. Otherwise, the value cannot be modified. | [optional] 


