

# ModelConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avs** | [**Avs**](Avs.md) | Describes the configuration for AVS ([Address Verification System](https://en.wikipedia.org/wiki/Address_Verification_System)). |  [optional] |
|**cardHolderName** | [**CardHolderNameEnum**](#CardHolderNameEnum) | Determines whether the cardholder name should be provided or not.  Permitted values: * NONE * OPTIONAL * REQUIRED |  [optional] |
|**installments** | [**InstallmentsNumber**](InstallmentsNumber.md) | Describes the configuration for [installment payments](https://docs.adyen.com/payment-methods/cards/credit-card-installments). |  [optional] |
|**shopperInput** | [**ShopperInput**](ShopperInput.md) | Determines how to display the details fields. |  [optional] |



## Enum: CardHolderNameEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| OPTIONAL | &quot;OPTIONAL&quot; |
| REQUIRED | &quot;REQUIRED&quot; |



