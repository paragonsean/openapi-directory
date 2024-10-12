# PayoneLinkApi.CartItemDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliveryDateEnd** | **Date** | delivery period end date | [optional] 
**deliveryDateStart** | **Date** | delivery date | [optional] 
**description** | **String** | item description | [optional] 
**number** | **String** | item number | 
**price** | **Number** | gross price of single item | 
**quantity** | **Number** | total number of ordered items | 
**type** | **String** | item type | 
**vatRate** | **Number** | vat rate (&lt;100 in %, &gt;&#x3D;100 in bp) | [optional] 



## Enum: TypeEnum


* `goods` (value: `"goods"`)

* `shipment` (value: `"shipment"`)

* `handling` (value: `"handling"`)

* `voucher` (value: `"voucher"`)




