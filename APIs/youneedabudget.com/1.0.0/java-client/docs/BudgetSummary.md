

# BudgetSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | [**List&lt;Account&gt;**](Account.md) | The budget accounts (only included if &#x60;include_accounts&#x3D;true&#x60; specified as query parameter) |  [optional] |
|**currencyFormat** | [**CurrencyFormat**](CurrencyFormat.md) |  |  [optional] |
|**dateFormat** | [**DateFormat**](DateFormat.md) |  |  [optional] |
|**firstMonth** | **LocalDate** | The earliest budget month |  [optional] |
|**id** | **UUID** |  |  |
|**lastModifiedOn** | **OffsetDateTime** | The last time any changes were made to the budget from either a web or mobile client |  [optional] |
|**lastMonth** | **LocalDate** | The latest budget month |  [optional] |
|**name** | **String** |  |  |



