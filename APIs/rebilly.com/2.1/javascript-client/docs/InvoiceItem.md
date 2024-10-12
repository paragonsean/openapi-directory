# RebillyRestApi.InvoiceItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**[InvoiceItemEmbeddedInner]**](InvoiceItemEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[InvoiceItemLinksInner]**](InvoiceItemLinksInner.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | Invoice item created time. | [optional] [readonly] 
**description** | **String** | Invoice item&#39;s description. | [optional] 
**discountAmount** | **Number** | Invoice item discount amount. | [optional] [readonly] 
**id** | **String** | The website identifier string. | [optional] [readonly] 
**periodEndTime** | **Date** | End time. | [optional] 
**periodNumber** | **Number** | Invoice item subscription order period number. | [optional] 
**periodStartTime** | **Date** | Start time. | [optional] 
**price** | **Number** | Invoice item&#39;s total price. | [optional] [readonly] 
**productId** | **String** | The product&#39;s ID. | [optional] 
**quantity** | **Number** | Invoice item&#39;s quantity. | [optional] 
**type** | **String** | Invoice item&#39;s type. | 
**unitPrice** | **Number** | Invoice item&#39;s price. | 
**updatedTime** | **Date** | Invoice item updated time. | [optional] [readonly] 



## Enum: TypeEnum


* `debit` (value: `"debit"`)

* `credit` (value: `"credit"`)




