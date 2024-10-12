

# DerivedTransactionsSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categorySummary** | [**List&lt;DerivedCategorySummary&gt;**](DerivedCategorySummary.md) | Summary of transaction amouts at category level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; |  [optional] [readonly] |
|**categoryType** | [**CategoryTypeEnum**](#CategoryTypeEnum) | Type of categories provided by transactions/categories service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**creditTotal** | [**Money**](Money.md) |  |  [optional] |
|**debitTotal** | [**Money**](Money.md) |  |  [optional] |
|**links** | [**DerivedTransactionsLinks**](DerivedTransactionsLinks.md) |  |  [optional] |



## Enum: CategoryTypeEnum

| Name | Value |
|---- | -----|
| TRANSFER | &quot;TRANSFER&quot; |
| DEFERRED_COMPENSATION | &quot;DEFERRED_COMPENSATION&quot; |
| UNCATEGORIZE | &quot;UNCATEGORIZE&quot; |
| INCOME | &quot;INCOME&quot; |
| EXPENSE | &quot;EXPENSE&quot; |



