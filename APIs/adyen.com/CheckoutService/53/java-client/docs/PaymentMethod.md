

# PaymentMethod


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brands** | **List&lt;String&gt;** | List of possible brands. For example: visa, mc. |  [optional] |
|**_configuration** | **Map&lt;String, String&gt;** | The configuration of the payment method. |  [optional] |
|**details** | [**List&lt;InputDetail&gt;**](InputDetail.md) | All input details to be provided to complete the payment with this payment method. |  [optional] |
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source of the payment method. |  [optional] |
|**group** | [**PaymentMethodGroup**](PaymentMethodGroup.md) | The group where this payment method belongs to. |  [optional] |
|**inputDetails** | [**List&lt;InputDetail&gt;**](InputDetail.md) | All input details to be provided to complete the payment with this payment method. |  [optional] |
|**name** | **String** | The displayable name of this payment method. |  [optional] |
|**supportsRecurring** | **Boolean** | Indicates whether this payment method supports tokenization or not. |  [optional] |
|**type** | **String** | The unique payment method code. |  [optional] |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



