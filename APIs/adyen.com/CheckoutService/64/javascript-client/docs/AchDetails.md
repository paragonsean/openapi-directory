# AdyenCheckoutApi.AchDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankAccountNumber** | **String** | The bank account number (without separators). | 
**bankAccountType** | **String** | The bank account type (checking, savings...). | [optional] 
**bankLocationId** | **String** | The bank routing number of the account. The field value is &#x60;nil&#x60; in most cases. | [optional] 
**encryptedBankAccountNumber** | **String** | Encrypted bank account number. The bank account number (without separators). | [optional] 
**encryptedBankLocationId** | **String** | Encrypted location id. The bank routing number of the account. The field value is &#x60;nil&#x60; in most cases. | [optional] 
**ownerName** | **String** | The name of the bank account holder. If you submit a name with non-Latin characters, we automatically replace some of them with corresponding Latin characters to meet the FATF recommendations. For example: * χ12 is converted to ch12. * üA is converted to euA. * Peter Møller is converted to Peter Mller, because banks don&#39;t accept &#39;ø&#39;. After replacement, the ownerName must have at least three alphanumeric characters (A-Z, a-z, 0-9), and at least one of them must be a valid Latin character (A-Z, a-z). For example: * John17 - allowed. * J17 - allowed. * 171 - not allowed. * John-7 - allowed. &gt; If provided details don&#39;t match the required format, the response returns the error message: 203 &#39;Invalid bank account holder name&#39;. | [optional] 
**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. | [optional] 
**type** | **String** | **ach** | [optional] [default to &#39;ach&#39;]



## Enum: BankAccountTypeEnum


* `balance` (value: `"balance"`)

* `checking` (value: `"checking"`)

* `deposit` (value: `"deposit"`)

* `general` (value: `"general"`)

* `other` (value: `"other"`)

* `payment` (value: `"payment"`)

* `savings` (value: `"savings"`)





## Enum: TypeEnum


* `ach` (value: `"ach"`)

* `ach_plaid` (value: `"ach_plaid"`)




