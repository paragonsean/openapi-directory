# AdyenCheckoutApi.Avs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressEditable** | **Boolean** | Indicates whether the shopper is allowed to modify the billing address for the current payment request. | [optional] 
**enabled** | **String** | Specifies whether the shopper should enter their billing address during checkout.  Allowed values: * yes — Perform AVS checks for every card payment. * automatic — Perform AVS checks only when required to optimize the conversion rate. * no — Do not perform AVS checks. | [optional] 



## Enum: EnabledEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)

* `automatic` (value: `"automatic"`)




