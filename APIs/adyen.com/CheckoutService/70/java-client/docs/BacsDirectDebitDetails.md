

# BacsDirectDebitDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccountNumber** | **String** | The bank account number (without separators). |  [optional] |
|**bankLocationId** | **String** | The bank routing number of the account. |  [optional] |
|**checkoutAttemptId** | **String** | The checkout attempt identifier. |  [optional] |
|**holderName** | **String** | The name of the bank account holder. |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **directdebit_GB** |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DIRECTDEBIT_GB | &quot;directdebit_GB&quot; |



