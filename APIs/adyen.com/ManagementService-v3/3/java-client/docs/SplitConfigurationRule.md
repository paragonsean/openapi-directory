

# SplitConfigurationRule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | **String** | The currency condition that defines whether the split logic applies. Its value must be a three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). |  |
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source condition of the payment method (only for cards).  Possible values: **credit**, **debit**, or **ANY**. |  [optional] |
|**paymentMethod** | **String** | The payment method condition that defines whether the split logic applies.  Possible values: * [Payment method variant](https://docs.adyen.com/development-resources/paymentmethodvariant): Apply the split logic for a specific payment method. * **ANY**: Apply the split logic for all available payment methods. |  |
|**ruleId** | **String** | The unique identifier of the split configuration rule. |  [optional] [readonly] |
|**shopperInteraction** | [**ShopperInteractionEnum**](#ShopperInteractionEnum) | The sales channel condition that defines whether the split logic applies.  Possible values: * **Ecommerce**: Online transactions where the cardholder is present. * **ContAuth**: Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). * **Moto**: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email or telephone. * **POS**: Point-of-sale transactions where the customer is physically present to make a payment using a secure payment terminal. * **ANY**: All sales channels. |  |
|**splitLogic** | [**SplitConfigurationLogic**](SplitConfigurationLogic.md) | Contains the split logic that is applied if the rule conditions are met. |  |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |
| ANY | &quot;ANY&quot; |



## Enum: ShopperInteractionEnum

| Name | Value |
|---- | -----|
| ECOMMERCE | &quot;Ecommerce&quot; |
| CONT_AUTH | &quot;ContAuth&quot; |
| MOTO | &quot;Moto&quot; |
| POS | &quot;POS&quot; |
| ANY | &quot;ANY&quot; |



