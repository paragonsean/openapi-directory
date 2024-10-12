# SwissNextGenBankingApiFramework.AccountAccess

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**[AccountReference16CH]**](AccountReference16CH.md) | Is asking for detailed account information.   If the array is empty in a request, the TPP is asking for an accessible account list.  This may be restricted in a PSU/ASPSP authorization dialogue.  If the array is empty, also the arrays for balances, additionalInformation sub attributes or transactions shall be empty, if used.  | [optional] 
**additionalInformation** | [**AdditionalInformationAccess**](AdditionalInformationAccess.md) |  | [optional] 
**allPsd2** | **String** | Optional if supported by API provider.  The values \&quot;allAccounts\&quot; and \&quot;allAccountsWithOwnerName\&quot; are admitted.  The support of the \&quot;allAccountsWithOwnerName\&quot; value by the ASPSP is optional.  | [optional] 
**availableAccounts** | **String** | Optional if supported by API provider.  The values \&quot;allAccounts\&quot; and \&quot;allAccountsWithOwnerName\&quot; are admitted.  The support of the \&quot;allAccountsWithOwnerName\&quot; value by the ASPSP is optional.  | [optional] 
**availableAccountsWithBalance** | **String** | Optional if supported by API provider.  The values \&quot;allAccounts\&quot; and \&quot;allAccountsWithOwnerName\&quot; are admitted.  The support of the \&quot;allAccountsWithOwnerName\&quot; value by the ASPSP is optional.  | [optional] 
**balances** | [**[AccountReference16CH]**](AccountReference16CH.md) | Is asking for balances of the addressed accounts.  If the array is empty in the request, the TPP is asking for the balances of all accessible account lists.  This may be restricted in a PSU/ASPSP authorization dialogue.  If the array is empty, also the arrays for accounts, additionalInformation sub attributes or transactions shall be empty, if used.  | [optional] 
**restrictedTo** | **[String]** | If the TPP requests access to accounts via availableAccounts (List of available accounts), global  or bank driven consents, the TPP may include this element to restrict access to the referred  account types. Absence of the element is interpreted as \&quot;no restriction\&quot; (therefore access to  accounts of all types is requested). The element may only occur, if each of the elements    - accounts    - balances    - transactions  is either not present or contains an empty array.   | [optional] 
**transactions** | [**[AccountReference16CH]**](AccountReference16CH.md) | Is asking for transactions of the addressed accounts.   If the array is empty in the request, the TPP is asking for the transactions of all accessible account lists.  This may be restricted in a PSU/ASPSP authorization dialogue.  If the array is empty, also the arrays for accounts, additionalInformation sub attributes or balances shall be empty, if used.  | [optional] 



## Enum: AllPsd2Enum


* `allAccounts` (value: `"allAccounts"`)

* `allAccountsWithOwnerName` (value: `"allAccountsWithOwnerName"`)





## Enum: AvailableAccountsEnum


* `allAccounts` (value: `"allAccounts"`)

* `allAccountsWithOwnerName` (value: `"allAccountsWithOwnerName"`)





## Enum: AvailableAccountsWithBalanceEnum


* `allAccounts` (value: `"allAccounts"`)

* `allAccountsWithOwnerName` (value: `"allAccountsWithOwnerName"`)




