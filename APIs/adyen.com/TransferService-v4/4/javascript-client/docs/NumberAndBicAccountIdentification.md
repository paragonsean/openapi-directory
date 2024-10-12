# TransfersApi.NumberAndBicAccountIdentification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The bank account number, without separators or whitespace. The length and format depends on the bank or country. | 
**additionalBankIdentification** | [**AdditionalBankIdentification**](AdditionalBankIdentification.md) | Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers. | [optional] 
**bic** | **String** | The bank&#39;s 8- or 11-character BIC or SWIFT code. | 
**type** | **String** | **numberAndBic** | [default to &#39;numberAndBic&#39;]



## Enum: TypeEnum


* `numberAndBic` (value: `"numberAndBic"`)




