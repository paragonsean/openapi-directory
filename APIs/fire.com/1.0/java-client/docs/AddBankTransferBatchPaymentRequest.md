

# AddBankTransferBatchPaymentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Long** | The value of the transaction |  [optional] |
|**destAccountHolderName** | **String** | The destination account holder name |  [optional] |
|**destAccountNumber** | **String** | The destination Account Number if a GBP bank transfer |  [optional] |
|**destIban** | **String** | The destination IBAN if a Euro Bank transfer |  [optional] |
|**destNsc** | **String** | The destination Nsc if a GBP bank transfer |  [optional] |
|**icanFrom** | **Long** | The Fire account ID for the fire.com account the funds are taken from. |  [optional] |
|**myRef** | **String** | The reference on the transaction for your records - not shown to the beneficiary. |  [optional] |
|**payeeType** | [**PayeeTypeEnum**](#PayeeTypeEnum) | Use PAYEE_ID if you are paying existing approved payees (Mode 1). |  [optional] |
|**yourRef** | **String** | The reference on the transaction - displayed on the beneficiary bank statement. |  [optional] |
|**payeeId** | **Long** | The ID of the existing or automatically created payee |  [optional] |



## Enum: PayeeTypeEnum

| Name | Value |
|---- | -----|
| PAYEE_ID | &quot;PAYEE_ID&quot; |



