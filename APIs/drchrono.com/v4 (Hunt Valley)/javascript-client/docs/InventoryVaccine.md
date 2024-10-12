# OpenapiJsClient.InventoryVaccine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **Number** | ID of &#x60;/api/inventory_categories&#x60; | [optional] 
**cost** | **Number** | Base cost for consumables. | [optional] 
**createdAt** | **String** |  | [optional] [readonly] 
**currentQuantity** | **Number** | This field can onlyu be changed by creating new patient vaccine record. Current quantity of an inventory vaccine is calculated by subtract number of records pointing to this inventory from the original quantity value. | [optional] [readonly] 
**cvxCode** | **String** |  | [optional] 
**doctor** | **Number** |  | 
**expiry** | **String** | When will the vaccine expire | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lotNumber** | **String** |  | [optional] 
**manufacturer** | **String** |  | [optional] 
**manufacturerCode** | **String** |  | 
**name** | **String** |  | 
**note** | **String** |  | [optional] 
**originalQuantity** | **Number** | Default to zero | [optional] 
**price** | **Number** |  | [optional] 
**priceWithTax** | **Number** |  | [optional] 
**salesTaxApplicable** | **Boolean** | Is sales tax applicable to this service/product? Default to false | [optional] 
**status** | **String** | Status of vaccine, could be one of &#x60;active&#x60;, &#x60;inactive&#x60;, &#x60;archived&#x60;, &#x60;voided&#x60;, default to &#x60;active&#x60; | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 
**vaccinationType** | **String** | Default to &#x60;\&quot;standard vaccine\&quot;&#x60; | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `archived` (value: `"archived"`)

* `voided` (value: `"voided"`)




