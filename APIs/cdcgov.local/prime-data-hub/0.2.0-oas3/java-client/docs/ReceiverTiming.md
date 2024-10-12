

# ReceiverTiming

When the report is sent if not immediately

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dailyAt** | **BigDecimal** | The UTC hour to send a daily batch |  [optional] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | How often send a report |  |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| REAL_TIME | &quot;REAL_TIME&quot; |
| HOURLY | &quot;HOURLY&quot; |
| DAILY | &quot;DAILY&quot; |



