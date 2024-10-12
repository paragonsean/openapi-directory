

# BalanceDetails

An array to specify multiple currency balances of an account

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balance** | **Double** | The opening balances of the account. Debits are positive, credits are negative values |  [optional] |
|**currencyCode** | **String** | The currency of the balance (Not required for base currency) |  [optional] |
|**currencyRate** | **Double** | (Optional) Exchange rate to base currency when money is spent or received. If not specified, XE rate for the day is applied |  [optional] |



