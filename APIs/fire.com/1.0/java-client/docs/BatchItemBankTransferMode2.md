

# BatchItemBankTransferMode2


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
|**payeeType** | [**PayeeTypeEnum**](#PayeeTypeEnum) | Use ACCOUNT_DETAILS if you are providing account numbers/sort codes/IBANs (Mode 2). Specify the account details in the destIban, destAccountHolderName, destNsc or destAccountNumber fields as appropriate. |  [optional] |
|**yourRef** | **String** | The reference on the transaction - displayed on the beneficiary bank statement. |  [optional] |



## Enum: PayeeTypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_DETAILS | &quot;ACCOUNT_DETAILS&quot; |



