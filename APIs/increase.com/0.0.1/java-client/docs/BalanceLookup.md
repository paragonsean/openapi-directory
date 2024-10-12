

# BalanceLookup

Represents a request to lookup the balance of an Account at a given point in time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The identifier for the account for which the balance was queried. |  |
|**availableBalance** | **Integer** | The Account&#39;s available balance, representing the current balance less any open Pending Transactions on the Account. |  |
|**currentBalance** | **Integer** | The Account&#39;s current balance, representing the sum of all posted Transactions on the Account. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;balance_lookup&#x60;. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BALANCE_LOOKUP | &quot;balance_lookup&quot; |



