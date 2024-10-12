# AdyenCheckoutApi.RecurringDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brands** | **[String]** | List of possible brands. For example: visa, mc. | [optional] 
**configuration** | **{String: String}** | The configuration of the payment method. | [optional] 
**details** | [**[InputDetail]**](InputDetail.md) | All input details to be provided to complete the payment with this payment method. | [optional] 
**fundingSource** | **String** | The funding source of the payment method. | [optional] 
**group** | [**PaymentMethodGroup**](PaymentMethodGroup.md) | The group where this payment method belongs to. | [optional] 
**inputDetails** | [**[InputDetail]**](InputDetail.md) | All input details to be provided to complete the payment with this payment method. | [optional] 
**name** | **String** | The displayable name of this payment method. | [optional] 
**recurringDetailReference** | **String** | The reference that uniquely identifies the recurring detail. | [optional] 
**storedDetails** | [**StoredDetails**](StoredDetails.md) | Contains information on previously stored payment details. | [optional] 
**supportsRecurring** | **Boolean** | Indicates whether this payment method supports tokenization or not. | [optional] 
**type** | **String** | The unique payment method code. | [optional] 



## Enum: FundingSourceEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)




