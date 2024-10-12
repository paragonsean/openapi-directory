# CatalogApi.ApiCatalogPvtProductProductIdSpecificationPost200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldId** | **Number** | Specification ID. | [optional] 
**fieldValueId** | **Number** | Specification Value ID. Mandatory for &#x60;FieldTypeId&#x60; &#x60;5&#x60;, &#x60;6&#x60; and &#x60;7&#x60;. Must not be used for any other field types | [optional] 
**id** | **Number** | ID of the association of the specification and the product. This ID is used to update or delete the specification. | [optional] 
**productId** | **Number** | Product ID. | [optional] 
**text** | **String** | Value of specification. Only for &#x60;FieldTypeId&#x60; different from &#x60;5&#x60;, &#x60;6&#x60; and &#x60;7&#x60;. | [optional] 


