# FireFinancialServicesBusinessApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **Number** | the balance of the account (in minor currency units - pence, cent etc. 434050 &#x3D;&#x3D; 4,340.50 GBP for a GBP account). | [optional] 
**cbic** | **String** | the BIC of the account (provided if currency is EUR). | [optional] 
**ccan** | **String** | the Account Number of the account. | [optional] 
**ciban** | **String** | the IBAN of the account (provided if currency is EUR). | [optional] 
**cnsc** | **String** | the Sort Code of the account. | [optional] 
**colour** | **String** | Internal Use | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**defaultAccount** | **Boolean** | true if this is the default account for this currency. This will be the account that general fees are taken from (as opposed to per-transaction fees). | [optional] 
**directDebitsAllowed** | **Boolean** | Whether or not direct debits can be set up on this account. | [optional] 
**fopOnly** | **Boolean** | Indicates that this account is for collecting Fire Open Payments only. All other payments to this account will be returned. | [optional] 
**ican** | **Number** | identifier for the fire.com account (assigned by fire.com) | [optional] 
**name** | **String** | the name the user gives to the account to help them identify it. | [optional] 
**status** | **String** | Live accounts can be used as normal. Migrated accounts were used before Brexit and are read-only. | [optional] 



## Enum: StatusEnum


* `LIVE` (value: `"LIVE"`)

* `BREXIT_MIGRATED` (value: `"BREXIT_MIGRATED"`)




