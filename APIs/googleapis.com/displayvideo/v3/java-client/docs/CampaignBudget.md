

# CampaignBudget

Settings that control how the campaign budget is allocated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetAmountMicros** | **String** | Required. The total amount the linked insertion order segments can budget. The amount is in micros. Must be greater than 0. For example, 500000000 represents 500 standard units of the currency. |  [optional] |
|**budgetId** | **String** | The unique ID of the campaign budget. Assigned by the system. Do not set for new budgets. Must be included when updating or adding budgets to campaign_budgets. Otherwise, a new ID will be generated and assigned. |  [optional] |
|**budgetUnit** | [**BudgetUnitEnum**](#BudgetUnitEnum) | Required. Immutable. Specifies whether the budget is measured in currency or impressions. |  [optional] |
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**displayName** | **String** | Required. The display name of the budget. Must be UTF-8 encoded with a maximum size of 240 bytes. |  [optional] |
|**externalBudgetId** | **String** | Immutable. The ID identifying this budget to the external source. If this field is set and the invoice detail level of the corresponding billing profile is set to \&quot;Budget level PO\&quot;, all impressions served against this budget will include this ID on the invoice. Must be unique under the campaign. |  [optional] |
|**externalBudgetSource** | [**ExternalBudgetSourceEnum**](#ExternalBudgetSourceEnum) | Required. The external source of the budget. |  [optional] |
|**invoiceGroupingId** | **String** | Immutable. The ID used to group budgets to be included the same invoice. If this field is set and the invoice level of the corresponding billing profile is set to \&quot;Budget invoice grouping ID\&quot;, all external_budget_id sharing the same invoice_grouping_id will be grouped in the same invoice. |  [optional] |
|**prismaConfig** | [**PrismaConfig**](PrismaConfig.md) |  |  [optional] |



## Enum: BudgetUnitEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BUDGET_UNIT_UNSPECIFIED&quot; |
| CURRENCY | &quot;BUDGET_UNIT_CURRENCY&quot; |
| IMPRESSIONS | &quot;BUDGET_UNIT_IMPRESSIONS&quot; |



## Enum: ExternalBudgetSourceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;EXTERNAL_BUDGET_SOURCE_UNSPECIFIED&quot; |
| NONE | &quot;EXTERNAL_BUDGET_SOURCE_NONE&quot; |
| MEDIA_OCEAN | &quot;EXTERNAL_BUDGET_SOURCE_MEDIA_OCEAN&quot; |



