

# SepaDirectDebitDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkoutAttemptId** | **String** | The checkout attempt identifier. |  [optional] |
|**iban** | **String** | The International Bank Account Number (IBAN). |  |
|**ownerName** | **String** | The name of the bank account holder. |  |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **sepadirectdebit** |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SEPADIRECTDEBIT | &quot;sepadirectdebit&quot; |
| SEPADIRECTDEBIT_AMAZONPAY | &quot;sepadirectdebit_amazonpay&quot; |



