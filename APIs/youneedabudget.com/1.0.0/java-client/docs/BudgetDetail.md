

# BudgetDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | [**List&lt;Account&gt;**](Account.md) |  |  [optional] |
|**currencyFormat** | [**CurrencyFormat**](CurrencyFormat.md) |  |  [optional] |
|**dateFormat** | [**DateFormat**](DateFormat.md) |  |  [optional] |
|**firstMonth** | **LocalDate** | The earliest budget month |  [optional] |
|**id** | **UUID** |  |  |
|**lastModifiedOn** | **OffsetDateTime** | The last time any changes were made to the budget from either a web or mobile client |  [optional] |
|**lastMonth** | **LocalDate** | The latest budget month |  [optional] |
|**name** | **String** |  |  |
|**categories** | [**List&lt;Category&gt;**](Category.md) |  |  [optional] |
|**categoryGroups** | [**List&lt;CategoryGroup&gt;**](CategoryGroup.md) |  |  [optional] |
|**months** | [**List&lt;MonthDetail&gt;**](MonthDetail.md) |  |  [optional] |
|**payeeLocations** | [**List&lt;PayeeLocation&gt;**](PayeeLocation.md) |  |  [optional] |
|**payees** | [**List&lt;Payee&gt;**](Payee.md) |  |  [optional] |
|**scheduledSubtransactions** | [**List&lt;ScheduledSubTransaction&gt;**](ScheduledSubTransaction.md) |  |  [optional] |
|**scheduledTransactions** | [**List&lt;ScheduledTransactionSummary&gt;**](ScheduledTransactionSummary.md) |  |  [optional] |
|**subtransactions** | [**List&lt;SubTransaction&gt;**](SubTransaction.md) |  |  [optional] |
|**transactions** | [**List&lt;TransactionSummary&gt;**](TransactionSummary.md) |  |  [optional] |



