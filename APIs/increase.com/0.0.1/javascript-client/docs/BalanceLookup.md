# IncreaseApi.BalanceLookup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The identifier for the account for which the balance was queried. | 
**availableBalance** | **Number** | The Account&#39;s available balance, representing the current balance less any open Pending Transactions on the Account. | 
**currentBalance** | **Number** | The Account&#39;s current balance, representing the sum of all posted Transactions on the Account. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;balance_lookup&#x60;. | 



## Enum: TypeEnum


* `balance_lookup` (value: `"balance_lookup"`)




