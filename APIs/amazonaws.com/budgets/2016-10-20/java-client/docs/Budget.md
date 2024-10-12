

# Budget

<p>Represents the output of the <code>CreateBudget</code> operation. The content consists of the detailed metadata and data file information, and the current status of the <code>budget</code> object.</p> <p>This is the Amazon Resource Name (ARN) pattern for a budget: </p> <p> <code>arn:aws:budgets::AccountId:budget/budgetName</code> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetName** | [**String**](String.md) |  |  |
|**budgetLimit** | [**BudgetBudgetLimit**](BudgetBudgetLimit.md) |  |  [optional] |
|**plannedBudgetLimits** | [**Map**](Map.md) |  |  [optional] |
|**costFilters** | [**Map**](Map.md) |  |  [optional] |
|**costTypes** | [**BudgetCostTypes**](BudgetCostTypes.md) |  |  [optional] |
|**timeUnit** | [**TimeUnit**](TimeUnit.md) |  |  |
|**timePeriod** | [**BudgetTimePeriod**](BudgetTimePeriod.md) |  |  [optional] |
|**calculatedSpend** | [**BudgetCalculatedSpend**](BudgetCalculatedSpend.md) |  |  [optional] |
|**budgetType** | [**BudgetType**](BudgetType.md) |  |  |
|**lastUpdatedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**autoAdjustData** | [**BudgetAutoAdjustData**](BudgetAutoAdjustData.md) |  |  [optional] |



