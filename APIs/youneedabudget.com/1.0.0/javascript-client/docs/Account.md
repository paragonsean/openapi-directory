# YnabApiEndpoints.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **Number** | The current balance of the account in milliunits format | 
**clearedBalance** | **Number** | The current cleared balance of the account in milliunits format | 
**closed** | **Boolean** | Whether this account is closed or not | 
**debtEscrowAmounts** | **{String: Number}** |  | [optional] 
**debtInterestRates** | **{String: Number}** |  | [optional] 
**debtMinimumPayments** | **{String: Number}** |  | [optional] 
**debtOriginalBalance** | **Number** | The original debt/loan account balance, specified in milliunits format. | [optional] 
**deleted** | **Boolean** | Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests. | 
**directImportInError** | **Boolean** | If an account linked to a financial institution (direct_import_linked&#x3D;true) and the linked connection is not in a healthy state, this will be true. | [optional] 
**directImportLinked** | **Boolean** | Whether or not the account is linked to a financial institution for automatic transaction import. | [optional] 
**id** | **String** |  | 
**lastReconciledAt** | **Date** | A date/time specifying when the account was last reconciled. | [optional] 
**name** | **String** |  | 
**note** | **String** |  | [optional] 
**onBudget** | **Boolean** | Whether this account is on budget or not | 
**transferPayeeId** | **String** | The payee id which should be used when transferring to this account | 
**type** | [**AccountType**](AccountType.md) |  | 
**unclearedBalance** | **Number** | The current uncleared balance of the account in milliunits format | 


