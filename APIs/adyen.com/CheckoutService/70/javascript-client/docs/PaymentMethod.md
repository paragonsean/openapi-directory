# AdyenCheckoutApi.PaymentMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **String** | Brand for the selected gift card. For example: plastix, hmclub. | [optional] 
**brands** | **[String]** | List of possible brands. For example: visa, mc. | [optional] 
**configuration** | **{String: String}** | The configuration of the payment method. | [optional] 
**fundingSource** | **String** | The funding source of the payment method. | [optional] 
**group** | [**PaymentMethodGroup**](PaymentMethodGroup.md) | The group where this payment method belongs to. | [optional] 
**inputDetails** | [**[InputDetail]**](InputDetail.md) | All input details to be provided to complete the payment with this payment method. | [optional] 
**issuers** | [**[PaymentMethodIssuer]**](PaymentMethodIssuer.md) | A list of issuers for this payment method. | [optional] 
**name** | **String** | The displayable name of this payment method. | [optional] 
**type** | **String** | The unique payment method code. | [optional] 



## Enum: FundingSourceEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)




