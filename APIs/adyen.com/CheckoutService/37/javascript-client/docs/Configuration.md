# AdyenCheckoutApi.Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avs** | [**Avs**](Avs.md) | Describes the configuration for AVS ([Address Verification System](https://en.wikipedia.org/wiki/Address_Verification_System)). | [optional] 
**cardHolderName** | **String** | Determines whether the cardholder name should be provided or not.  Permitted values: * NONE * OPTIONAL * REQUIRED | [optional] 
**installments** | [**InstallmentsNumber**](InstallmentsNumber.md) | Describes the configuration for [installment payments](https://docs.adyen.com/payment-methods/cards/credit-card-installments). | [optional] 
**shopperInput** | [**ShopperInput**](ShopperInput.md) | Determines how to display the details fields. | [optional] 



## Enum: CardHolderNameEnum


* `NONE` (value: `"NONE"`)

* `OPTIONAL` (value: `"OPTIONAL"`)

* `REQUIRED` (value: `"REQUIRED"`)




