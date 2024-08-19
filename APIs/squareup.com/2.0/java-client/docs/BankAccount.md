

# BankAccount

Represents a bank account. For more information about  linking a bank account to a Square account, see  [Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumberSuffix** | **String** | The last few digits of the account number. |  |
|**accountType** | **String** | The financial purpose of the associated bank account. |  |
|**bankName** | **String** | Read only. Name of actual financial institution.  For example \&quot;Bank of America\&quot;. |  [optional] |
|**country** | **String** | The ISO 3166 Alpha-2 country code where the bank account is based. |  |
|**creditable** | **Boolean** | Indicates whether it is possible for Square to send money to this bank account. |  |
|**currency** | **String** | The 3-character ISO 4217 currency code indicating the operating currency of the bank account. For example, the currency code for US dollars is &#x60;USD&#x60;. |  |
|**debitMandateReferenceId** | **String** | Reference identifier that will be displayed to UK bank account owners when collecting direct debit authorization. Only required for UK bank accounts. |  [optional] |
|**debitable** | **Boolean** | Indicates whether it is possible for Square to take money from this  bank account. |  |
|**fingerprint** | **String** | A Square-assigned, unique identifier for the bank account based on the account information. The account fingerprint can be used to compare account entries and determine if the they represent the same real-world bank account. |  [optional] |
|**holderName** | **String** | Name of the account holder. This name must match the name  on the targeted bank account record. |  |
|**id** | **String** | The unique, Square-issued identifier for the bank account. |  |
|**locationId** | **String** | The location to which the bank account belongs. |  [optional] |
|**primaryBankIdentificationNumber** | **String** | Primary identifier for the bank. For more information, see  [Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api). |  |
|**referenceId** | **String** | Client-provided identifier for linking the banking account to an entity in a third-party system (for example, a bank account number or a user identifier). |  [optional] |
|**secondaryBankIdentificationNumber** | **String** | Secondary identifier for the bank. For more information, see  [Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api). |  [optional] |
|**status** | **String** | Read-only. The current verification status of this BankAccount object. |  |
|**version** | **Integer** | The current version of the &#x60;BankAccount&#x60;. |  [optional] |



