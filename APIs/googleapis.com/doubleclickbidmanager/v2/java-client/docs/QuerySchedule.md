

# QuerySchedule

Information on when and how frequently to run a query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endDate** | [**Date**](Date.md) |  |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | How often the query is run. |  [optional] |
|**nextRunTimezoneCode** | **String** | Canonical timezone code for report generation time. Defaults to &#x60;America/New_York&#x60;. |  [optional] |
|**startDate** | [**Date**](Date.md) |  |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| FREQUENCY_UNSPECIFIED | &quot;FREQUENCY_UNSPECIFIED&quot; |
| ONE_TIME | &quot;ONE_TIME&quot; |
| DAILY | &quot;DAILY&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| SEMI_MONTHLY | &quot;SEMI_MONTHLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| QUARTERLY | &quot;QUARTERLY&quot; |
| YEARLY | &quot;YEARLY&quot; |



