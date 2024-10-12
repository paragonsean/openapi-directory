

# Period


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actualAmount** | **BigDecimal** | The sum of all actuals (transactions) in the period. |  [optional] |
|**currencyCode** | **String** | The currency of the period. |  [optional] |
|**current** | **Boolean** | Whether this period is current, such that the current date (in the user&#39;s time zone) falls within the date range. |  [optional] |
|**endDate** | **String** | The end date of the period. |  [optional] |
|**forecastAmount** | **BigDecimal** | The sum of all forecast sources (budget events) in the period, for comparison against the actual amount. |  [optional] |
|**overBudget** | **Boolean** | Whether the budget has been exceeded in the period. |  [optional] |
|**overBy** | **BigDecimal** | How much the budget has been exceeded by in the period. |  [optional] |
|**percentageUsed** | **BigDecimal** | The percentage of the budget that has been used in the period. |  [optional] |
|**refundAmount** | **BigDecimal** | This attribute tracks the amount that has been refunded or deducted to the actual amount. When a category is set to \&quot;always expense\&quot;, any credit transactions are treated as refunds and when set to \&quot;always income\&quot;, any debit transactions are treated as deductions. |  [optional] |
|**startDate** | **String** | The start date of the period. |  [optional] |
|**underBudget** | **Boolean** | Whether the budget has not been exceeded in the period. |  [optional] |
|**underBy** | **BigDecimal** | How much there is left in the budget for the period. |  [optional] |



