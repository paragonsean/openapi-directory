

# PaymentMethod


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | Brand for the selected gift card. For example: plastix, hmclub. |  [optional] |
|**brands** | **List&lt;String&gt;** | List of possible brands. For example: visa, mc. |  [optional] |
|**_configuration** | **Map&lt;String, String&gt;** | The configuration of the payment method. |  [optional] |
|**fundingSource** | [**FundingSourceEnum**](#FundingSourceEnum) | The funding source of the payment method. |  [optional] |
|**group** | [**PaymentMethodGroup**](PaymentMethodGroup.md) | The group where this payment method belongs to. |  [optional] |
|**inputDetails** | [**List&lt;InputDetail&gt;**](InputDetail.md) | All input details to be provided to complete the payment with this payment method. |  [optional] |
|**issuers** | [**List&lt;PaymentMethodIssuer&gt;**](PaymentMethodIssuer.md) | A list of issuers for this payment method. |  [optional] |
|**name** | **String** | The displayable name of this payment method. |  [optional] |
|**type** | **String** | The unique payment method code. |  [optional] |



## Enum: FundingSourceEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



