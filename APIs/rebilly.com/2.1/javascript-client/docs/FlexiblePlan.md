# RebillyRestApi.FlexiblePlan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The Plan identifier. | 
**createdTime** | **Date** | Plan created time. | [optional] [readonly] 
**currency** | **String** | ISO 4217 alphabetic currency code. | 
**currencySign** | **String** | Currency sign. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**isTrialOnly** | **Boolean** | Whether a plan has a trial without recurring instructions. | [optional] [readonly] 
**name** | **String** | The plan name, displayed on invoices and receipts. | 
**pricing** | [**PlanPriceFormula**](PlanPriceFormula.md) |  | 
**productId** | **String** | The related product ID. | 
**productOptions** | **{String: String}** | Name-value pairs to specify the product options. | [optional] 
**recurringInterval** | [**CommonPlanRecurringInterval**](CommonPlanRecurringInterval.md) |  | [optional] 
**revision** | **Number** | Increments when the plan is modified.  Compare to materialized subscription items revision.  | [optional] [readonly] 
**setup** | [**CommonPlanSetup**](CommonPlanSetup.md) |  | [optional] 
**trial** | [**CommonPlanTrial**](CommonPlanTrial.md) |  | [optional] 
**updatedTime** | **Date** | Plan updated time. | [optional] [readonly] 


