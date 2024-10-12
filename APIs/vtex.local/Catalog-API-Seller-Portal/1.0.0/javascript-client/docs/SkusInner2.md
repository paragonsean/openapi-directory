# CatalogApiSellerPortal.SkusInner2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**Dimensions**](Dimensions.md) |  | 
**ean** | **String** | Unique SKU identification code (barcode), composed of up to 13 numeric characters. | [optional] 
**externalId** | **String** | Unique reference code created to improve the store&#39;s organization. This is not a required field. | [optional] 
**id** | **String** | SKU unique identifier number. | 
**images** | **[Object]** | SKU&#39;s images IDs. | 
**isActive** | **Boolean** | If the SKU is active (&#x60;true&#x60;) or inactive (&#x60;false&#x60;). | 
**manufacturerCode** | **String** | SKU reference code in the store. | [optional] 
**specs** | [**[SpecsInner]**](SpecsInner.md) | SKU specifications. This field is mandatory, but nullable if there is only one SKU. | 
**weight** | **Number** | SKU weight. | 


