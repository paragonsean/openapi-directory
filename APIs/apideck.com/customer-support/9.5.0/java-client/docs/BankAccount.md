

# BankAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** | The name which you used in opening your bank account. |  [optional] |
|**accountNumber** | **String** | A bank account number is a number that is tied to your bank account. If you have several bank accounts, such as personal, joint, business (and so on), each account will have a different account number. |  [optional] |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The type of bank account. |  [optional] |
|**bankCode** | **String** | A bank code is a code assigned by a central bank, a bank supervisory body or a Bankers Association in a country to all its licensed member banks or financial institutions. |  [optional] |
|**bic** | **String** |  |  [optional] |
|**branchIdentifier** | **String** | A branch identifier is a unique identifier for a branch of a bank or financial institution. |  [optional] |
|**bsbNumber** | **String** | A BSB is a 6 digit numeric code used for identifying the branch of an Australian or New Zealand bank or financial institution. |  [optional] |
|**currency** | **Currency** |  |  [optional] |
|**iban** | **String** |  |  [optional] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| BANK_ACCOUNT | &quot;bank_account&quot; |
| CREDIT_CARD | &quot;credit_card&quot; |
| OTHER | &quot;other&quot; |



