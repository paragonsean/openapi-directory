# AccountingApi.BankAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | The name which you used in opening your bank account. | [optional] 
**accountNumber** | **String** | A bank account number is a number that is tied to your bank account. If you have several bank accounts, such as personal, joint, business (and so on), each account will have a different account number. | [optional] 
**accountType** | **String** | The type of bank account. | [optional] 
**bankCode** | **String** | A bank code is a code assigned by a central bank, a bank supervisory body or a Bankers Association in a country to all its licensed member banks or financial institutions. | [optional] 
**bankName** | **String** | The name of the bank | [optional] 
**bic** | **String** | The Bank Identifier Code (BIC). | [optional] 
**branchIdentifier** | **String** | A branch identifier is a unique identifier for a branch of a bank or financial institution. | [optional] 
**bsbNumber** | **String** | A BSB is a 6 digit numeric code used for identifying the branch of an Australian or New Zealand bank or financial institution. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**iban** | **String** | The International Bank Account Number (IBAN). | [optional] 
**routingNumber** | **String** | A routing number is a nine-digit code used to identify a financial institution in the United States. | [optional] 



## Enum: AccountTypeEnum


* `bank_account` (value: `"bank_account"`)

* `credit_card` (value: `"credit_card"`)

* `other` (value: `"other"`)




