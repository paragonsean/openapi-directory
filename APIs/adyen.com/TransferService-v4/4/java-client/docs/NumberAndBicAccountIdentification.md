

# NumberAndBicAccountIdentification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The bank account number, without separators or whitespace. The length and format depends on the bank or country. |  |
|**additionalBankIdentification** | [**AdditionalBankIdentification**](AdditionalBankIdentification.md) | Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers. |  [optional] |
|**bic** | **String** | The bank&#39;s 8- or 11-character BIC or SWIFT code. |  |
|**type** | [**TypeEnum**](#TypeEnum) | **numberAndBic** |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NUMBER_AND_BIC | &quot;numberAndBic&quot; |



