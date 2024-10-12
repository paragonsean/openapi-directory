# CostManagementClient.ViewProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accumulated** | **String** | Show costs accumulated over time. | [optional] 
**chart** | **String** | Chart type of the main view in Cost Analysis. Required. | [optional] 
**createdOn** | **Date** | Date the user created this view. | [optional] [readonly] 
**displayName** | **String** | User input name of the view. Required. | [optional] 
**kpis** | [**[KpiProperties]**](KpiProperties.md) | List of KPIs to show in Cost Analysis UI. | [optional] 
**metric** | **String** | Metric to use when displaying costs. | [optional] 
**modifiedOn** | **Date** | Date when the user last modified this view. | [optional] [readonly] 
**pivots** | [**[PivotProperties]**](PivotProperties.md) | Configuration of 3 sub-views in the Cost Analysis UI. | [optional] 
**query** | [**ReportConfigDefinition**](ReportConfigDefinition.md) |  | [optional] 
**scope** | **String** | Cost Management scope to save the view on. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for ExternalBillingAccount scope, and &#39;/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for ExternalSubscription scope. | [optional] 



## Enum: AccumulatedEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)





## Enum: ChartEnum


* `Area` (value: `"Area"`)

* `Line` (value: `"Line"`)

* `StackedColumn` (value: `"StackedColumn"`)

* `GroupedColumn` (value: `"GroupedColumn"`)

* `Table` (value: `"Table"`)





## Enum: MetricEnum


* `ActualCost` (value: `"ActualCost"`)

* `AmortizedCost` (value: `"AmortizedCost"`)

* `AHUB` (value: `"AHUB"`)




