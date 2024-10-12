# LinodeApi.PaymentMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When the Payment Method was added to the Account. | [optional] [readonly] 
**data** | [**PaymentMethodData**](PaymentMethodData.md) |  | [optional] 
**id** | **Number** | The unique ID of this Payment Method. | [optional] 
**isDefault** | **Boolean** | Whether this Payment Method is the default method for automatically processing service charges.  | [optional] 
**type** | **String** | The type of Payment Method. | [optional] 



## Enum: TypeEnum


* `credit_card` (value: `"credit_card"`)

* `google_pay` (value: `"google_pay"`)

* `paypal` (value: `"paypal"`)




