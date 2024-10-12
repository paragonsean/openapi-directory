

# Plan


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | Plan created time. |  [optional] [readonly] |
|**currency** | **String** | ISO 4217 alphabetic currency code. |  |
|**currencySign** | **String** | Currency sign. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**id** | **String** | The plan ID. |  [optional] [readonly] |
|**isTrialOnly** | **Boolean** | Whether a plan has a trial without recurring instructions. |  [optional] [readonly] |
|**name** | **String** | The plan name, displayed on invoices and receipts. |  |
|**pricing** | [**PlanPriceFormula**](PlanPriceFormula.md) |  |  |
|**productId** | **String** | The related product ID. |  |
|**productOptions** | **Map&lt;String, String&gt;** | Name-value pairs to specify the product options. |  [optional] |
|**recurringInterval** | [**CommonPlanRecurringInterval**](CommonPlanRecurringInterval.md) |  |  [optional] |
|**revision** | **Integer** | Increments when the plan is modified.  Compare to materialized subscription items revision.  |  [optional] [readonly] |
|**setup** | [**CommonPlanSetup**](CommonPlanSetup.md) |  |  [optional] |
|**trial** | [**CommonPlanTrial**](CommonPlanTrial.md) |  |  [optional] |
|**updatedTime** | **OffsetDateTime** | Plan updated time. |  [optional] [readonly] |
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**invoiceTimeShift** | [**InvoiceTimeShift**](InvoiceTimeShift.md) | You can shift issue time and due time of invoices for this plan. |  [optional] |



