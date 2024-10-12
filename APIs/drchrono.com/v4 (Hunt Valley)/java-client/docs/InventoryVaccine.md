

# InventoryVaccine


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **Integer** | ID of &#x60;/api/inventory_categories&#x60; |  [optional] |
|**cost** | **BigDecimal** | Base cost for consumables. |  [optional] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**currentQuantity** | **Integer** | This field can onlyu be changed by creating new patient vaccine record. Current quantity of an inventory vaccine is calculated by subtract number of records pointing to this inventory from the original quantity value. |  [optional] [readonly] |
|**cvxCode** | **String** |  |  [optional] |
|**doctor** | **Integer** |  |  |
|**expiry** | **String** | When will the vaccine expire |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lotNumber** | **String** |  |  [optional] |
|**manufacturer** | **String** |  |  [optional] |
|**manufacturerCode** | **String** |  |  |
|**name** | **String** |  |  |
|**note** | **String** |  |  [optional] |
|**originalQuantity** | **Integer** | Default to zero |  [optional] |
|**price** | **BigDecimal** |  |  [optional] |
|**priceWithTax** | **BigDecimal** |  |  [optional] |
|**salesTaxApplicable** | **Boolean** | Is sales tax applicable to this service/product? Default to false |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of vaccine, could be one of &#x60;active&#x60;, &#x60;inactive&#x60;, &#x60;archived&#x60;, &#x60;voided&#x60;, default to &#x60;active&#x60; |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |
|**vaccinationType** | **String** | Default to &#x60;\&quot;standard vaccine\&quot;&#x60; |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| ARCHIVED | &quot;archived&quot; |
| VOIDED | &quot;voided&quot; |



