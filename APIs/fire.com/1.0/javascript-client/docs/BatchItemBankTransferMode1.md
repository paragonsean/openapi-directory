# FireFinancialServicesBusinessApi.BatchItemBankTransferMode1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The value of the transaction | [optional] 
**icanFrom** | **Number** | The Fire account ID for the fire.com account the funds are taken from. | [optional] 
**myRef** | **String** | The reference on the transaction for your records - not shown to the beneficiary. | [optional] 
**payeeId** | **Number** | The ID of the existing or automatically created payee | [optional] 
**payeeType** | **String** | Use PAYEE_ID if you are paying existing approved payees (Mode 1). | [optional] 
**yourRef** | **String** | The reference on the transaction - displayed on the beneficiary bank statement. | [optional] 



## Enum: PayeeTypeEnum


* `PAYEE_ID` (value: `"PAYEE_ID"`)




