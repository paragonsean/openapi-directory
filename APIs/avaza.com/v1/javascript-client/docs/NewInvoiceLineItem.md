# AvazaApiDocumentation.NewInvoiceLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Plain UTF8 text. (no HTML) | [optional] 
**discount** | **Number** | Enter 10.5 to give a 10.5% discount | [optional] 
**inventoryItemIDFK** | **Number** | If not specified then Inventory Item Name must be specified. | [optional] 
**inventoryItemName** | **String** | If not specified then Inventory item ID must be specified. If specified and not matched to any existing inventory items then a new inventory item will be created. Max 200 characters. | [optional] 
**projectIDFK** | **Number** | Optional. Project ID of an Avaza Project that belongs to this customer, so line item is attributed to that Project for reporting. | [optional] 
**quantity** | **Number** | The quantity for the line item | 
**taxIDFK** | **Number** | If specified then it must match an existing Tax ID. If not specified then Tax Name and Tax Percent must be specified. | [optional] 
**taxName** | **String** | Must be specified if the Tax ID is blank. If the Tax Name is specified it will be matched to an existing Tax Name or else a new Tax will be created. | [optional] 
**taxPercent** | **Number** | The Tax Percent will only be used if a new tax is being created. | [optional] 
**unitPrice** | **Number** | The unit price for the lineitem. | 


