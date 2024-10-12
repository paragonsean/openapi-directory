# SwissNextGenBankingApiFramework.ReadCardAccountBalanceResponse200

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**[Balance]**](Balance.md) | A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance.  | 
**cardAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  | [optional] 
**debitAccounting** | **Boolean** | If true, the amounts of debits on the reports are quoted positive with the related consequence for balances. If false, the amount of debits on the reports are quoted negative.  | [optional] 


