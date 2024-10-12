

# ViewProperties

The properties of the view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accumulated** | [**AccumulatedEnum**](#AccumulatedEnum) | Show costs accumulated over time. |  [optional] |
|**chart** | [**ChartEnum**](#ChartEnum) | Chart type of the main view in Cost Analysis. Required. |  [optional] |
|**createdOn** | **OffsetDateTime** | Date the user created this view. |  [optional] [readonly] |
|**displayName** | **String** | User input name of the view. Required. |  [optional] |
|**kpis** | [**List&lt;KpiProperties&gt;**](KpiProperties.md) | List of KPIs to show in Cost Analysis UI. |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) | Metric to use when displaying costs. |  [optional] |
|**modifiedOn** | **OffsetDateTime** | Date when the user last modified this view. |  [optional] [readonly] |
|**pivots** | [**List&lt;PivotProperties&gt;**](PivotProperties.md) | Configuration of 3 sub-views in the Cost Analysis UI. |  [optional] |
|**query** | [**ReportConfigDefinition**](ReportConfigDefinition.md) |  |  [optional] |
|**scope** | **String** | Cost Management scope to save the view on. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for ExternalBillingAccount scope, and &#39;/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for ExternalSubscription scope. |  [optional] |



## Enum: AccumulatedEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |



## Enum: ChartEnum

| Name | Value |
|---- | -----|
| AREA | &quot;Area&quot; |
| LINE | &quot;Line&quot; |
| STACKED_COLUMN | &quot;StackedColumn&quot; |
| GROUPED_COLUMN | &quot;GroupedColumn&quot; |
| TABLE | &quot;Table&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| ACTUAL_COST | &quot;ActualCost&quot; |
| AMORTIZED_COST | &quot;AmortizedCost&quot; |
| AHUB | &quot;AHUB&quot; |



