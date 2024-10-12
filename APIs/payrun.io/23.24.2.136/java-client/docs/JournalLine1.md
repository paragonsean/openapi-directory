

# JournalLine1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credit** | **Double** | The journal lines&#39; credit |  [optional] |
|**debit** | **Double** | The journal lines&#39; debit |  [optional] |
|**description** | **String** | The journal lines&#39; description |  [optional] |
|**employee** | [**Employee3**](Employee3.md) |  |  [optional] |
|**generated** | **OffsetDateTime** | The journal lines&#39; generated |  [optional] |
|**grouping** | **String** | The journal lines&#39; grouping |  [optional] |
|**ledgerTarget** | **String** | The journal lines&#39; ledger target |  [optional] |
|**nomCode** | **String** | The journal lines&#39; nom code |  [optional] |
|**payFrequency** | [**PayFrequencyEnum**](#PayFrequencyEnum) | The journal lines&#39; pay frequency |  [optional] |
|**payRun** | [**PayRun2**](PayRun2.md) |  |  [optional] |
|**subContractor** | [**SubContractor2**](SubContractor2.md) |  |  [optional] |
|**subNomCode** | **String** | The journal lines&#39; sub nom code |  [optional] |
|**taxPeriod** | **Integer** | The journal lines&#39; tax period |  [optional] |
|**taxYear** | **Integer** | The journal lines&#39; tax year |  [optional] |



## Enum: PayFrequencyEnum

| Name | Value |
|---- | -----|
| WEEKLY | &quot;Weekly&quot; |
| MONTHLY | &quot;Monthly&quot; |
| TWO_WEEKLY | &quot;TwoWeekly&quot; |
| FOUR_WEEKLY | &quot;FourWeekly&quot; |
| YEARLY | &quot;Yearly&quot; |



