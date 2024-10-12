

# QuerySchedule

Information on how frequently and when to run a query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTimeMs** | **String** | Datetime to periodically run the query until. |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | How often the query is run. |  [optional] |
|**nextRunMinuteOfDay** | **Integer** | Time of day at which a new report will be generated, represented as minutes past midnight. Range is 0 to 1439. Only applies to scheduled reports. |  [optional] |
|**nextRunTimezoneCode** | **String** | Canonical timezone code for report generation time. Defaults to America/New_York. |  [optional] |
|**startTimeMs** | **String** | When to start running the query. Not applicable to &#x60;ONE_TIME&#x60; frequency. |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| ONE_TIME | &quot;ONE_TIME&quot; |
| DAILY | &quot;DAILY&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| SEMI_MONTHLY | &quot;SEMI_MONTHLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| QUARTERLY | &quot;QUARTERLY&quot; |
| YEARLY | &quot;YEARLY&quot; |



