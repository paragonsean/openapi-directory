

# Scenario


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**achieveDate** | **String** | For goals, the date that they should be achieved by. |  [optional] |
|**closingBalance** | **BigDecimal** | The closing balance of the scenario. |  [optional] |
|**closingBalanceDate** | **String** | The date of the closing balance. |  [optional] |
|**createdAt** | **String** | When the scenario was created. |  [optional] |
|**currentBalance** | **BigDecimal** | The current balance of the scenario. |  [optional] |
|**currentBalanceDate** | **String** | The date of the current balance. |  [optional] |
|**currentBalanceExchangeRate** | **BigDecimal** | The exchange rate between the scenario&#39;s currency and the user&#39;s base currency, when different. If the currencies are the same, null is returned. |  [optional] |
|**currentBalanceInBaseCurrency** | **BigDecimal** | The current balance of the scenario in the user&#39;s base currency. |  [optional] |
|**description** | **String** | A short description of what the scenario is modelling. |  [optional] |
|**id** | **Integer** | The unique identifier of the scenario. |  [optional] |
|**interestRate** | **BigDecimal** | The amount of interest to apply to the balance. Will apply periodically depending on what &#x60;interest_rate_repeat_id&#x60; is set to. |  [optional] |
|**interestRateRepeatId** | **Integer** | A number representing how often the interest should be applied. 0 is used for no interest, 2 is weekly, 3 is fortnightly, 4 is monthly, 5 is yearly and 7 for quarterly. |  [optional] |
|**maximumValue** | **BigDecimal** |  |  [optional] |
|**minimumValue** | **BigDecimal** |  |  [optional] |
|**safeBalance** | **BigDecimal** | The current safe balance in the user&#39;s base currency, if safe balance is activated on the account associated with the scenario. If safe balance is not activated, then null is returned. |  [optional] |
|**safeBalanceInBaseCurrency** | **BigDecimal** | The current safe balance in the user&#39;s base currency, if safe balance is activated on the account associated with the scenario. If safe balance is not available, then null is returned. |  [optional] |
|**startingBalance** | **BigDecimal** | The starting balance of the scenario. |  [optional] |
|**startingBalanceDate** | **String** | The date of the starting balance. |  [optional] |
|**title** | **String** | The title of the scenario. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the scenario. |  [optional] |
|**updatedAt** | **String** | When the scenario was last updated. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NO_INTEREST | &quot;no-interest&quot; |
| SAVINGS | &quot;savings&quot; |
| DEBT | &quot;debt&quot; |



