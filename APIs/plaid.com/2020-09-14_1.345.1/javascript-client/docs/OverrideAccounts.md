# ThePlaidApi.OverrideAccounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | ISO-4217 currency code. If provided, the account will be denominated in the given currency. Transactions will also be in this currency by default. | 
**forceAvailableBalance** | **Number** | If provided, the account will always have this amount as its  available balance, regardless of current balance or changes in transactions over time. | 
**holdings** | [**HoldingsOverride**](HoldingsOverride.md) |  | [optional] 
**identity** | [**OwnerOverride**](OwnerOverride.md) |  | 
**income** | [**IncomeOverride**](IncomeOverride.md) |  | [optional] 
**inflowModel** | [**InflowModel**](InflowModel.md) |  | 
**investmentTransactions** | [**InvestmentsTransactionsOverride**](InvestmentsTransactionsOverride.md) |  | [optional] 
**liability** | [**LiabilityOverride**](LiabilityOverride.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 
**numbers** | [**Numbers**](Numbers.md) |  | 
**startingBalance** | **Number** | If provided, the account will start with this amount as the current balance.  | 
**subtype** | [**AccountSubtype**](AccountSubtype.md) |  | 
**transactions** | [**[TransactionOverride]**](TransactionOverride.md) | Specify the list of transactions on the account. | 
**type** | [**OverrideAccountType**](OverrideAccountType.md) |  | 


