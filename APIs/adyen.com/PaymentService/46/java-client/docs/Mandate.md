

# Mandate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **String** | The billing amount (in minor units) of the recurring transactions. |  |
|**amountRule** | [**AmountRuleEnum**](#AmountRuleEnum) | The limitation rule of the billing amount.  Possible values:  * **max**: The transaction amount can not exceed the &#x60;amount&#x60;.   * **exact**: The transaction amount should be the same as the &#x60;amount&#x60;.   |  [optional] |
|**billingAttemptsRule** | [**BillingAttemptsRuleEnum**](#BillingAttemptsRuleEnum) | The rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring date.  Possible values:   * **on**: On a specific date.   * **before**:  Before and on a specific date.   * **after**: On and after a specific date.   |  [optional] |
|**billingDay** | **String** | The number of the day, on which the recurring debit can happen. Should be within the same calendar month as the mandate recurring date.  Possible values: 1-31 based on the &#x60;frequency&#x60;. |  [optional] |
|**endsAt** | **String** | End date of the billing plan, in YYYY-MM-DD format. |  |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | The frequency with which a shopper should be charged.  Possible values: **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**, **yearly**. |  |
|**remarks** | **String** | The message shown by UPI to the shopper on the approval screen. |  [optional] |
|**startsAt** | **String** | Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date. |  [optional] |



## Enum: AmountRuleEnum

| Name | Value |
|---- | -----|
| MAX | &quot;max&quot; |
| EXACT | &quot;exact&quot; |



## Enum: BillingAttemptsRuleEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| BEFORE | &quot;before&quot; |
| AFTER | &quot;after&quot; |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| ADHOC | &quot;adhoc&quot; |
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| BI_WEEKLY | &quot;biWeekly&quot; |
| MONTHLY | &quot;monthly&quot; |
| QUARTERLY | &quot;quarterly&quot; |
| HALF_YEARLY | &quot;halfYearly&quot; |
| YEARLY | &quot;yearly&quot; |



