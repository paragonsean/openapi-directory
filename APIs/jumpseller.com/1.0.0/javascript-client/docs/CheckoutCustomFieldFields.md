# JumpsellerApi.CheckoutCustomFieldFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **String** | Area of the CheckoutCustomField | [optional] 
**customFieldSelectOptions** | **[String]** | The values for the CheckoutCustomField selection | [optional] 
**deletable** | **Boolean** | True if the CheckoutCustomField can be removed from the store | [optional] [default to false]
**id** | **Number** | Unique identifier of the CheckoutCustomField | [optional] 
**label** | **String** | Label given to the CheckoutCustomField | [optional] 
**position** | **Number** | Position of the CheckoutCustomField | [optional] 
**required** | **Boolean** | True if the CheckoutCustomField is mandatory | [optional] [default to false]
**type** | **String** | Type of the CheckoutCustomField | [optional] 



## Enum: AreaEnum


* `contact` (value: `"contact"`)

* `billing_shipping` (value: `"billing_shipping"`)

* `other` (value: `"other"`)





## Enum: TypeEnum


* `text` (value: `"text"`)

* `select` (value: `"select"`)

* `input` (value: `"input"`)

* `checkbox` (value: `"checkbox"`)




