

# PayoutScheduleResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextScheduledPayout** | **OffsetDateTime** | The date of the next scheduled payout. |  [optional] |
|**schedule** | [**ScheduleEnum**](#ScheduleEnum) | The payout schedule of the account. Permitted values: &#x60;DEFAULT&#x60;, &#x60;DAILY&#x60;, &#x60;DAILY_US&#x60;, &#x60;DAILY_EU&#x60;, &#x60;DAILY_AU&#x60;, &#x60;DAILY_SG&#x60;, &#x60;WEEKLY&#x60;, &#x60;WEEKLY_ON_TUE_FRI_MIDNIGHT&#x60;, &#x60;BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT&#x60;, &#x60;MONTHLY&#x60;, &#x60;HOLD&#x60;. |  [optional] |



## Enum: ScheduleEnum

| Name | Value |
|---- | -----|
| BIWEEKLY_ON_1_ST_AND_15_TH_AT_MIDNIGHT | &quot;BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT&quot; |
| DAILY | &quot;DAILY&quot; |
| DAILY_AU | &quot;DAILY_AU&quot; |
| DAILY_EU | &quot;DAILY_EU&quot; |
| DAILY_SG | &quot;DAILY_SG&quot; |
| DAILY_US | &quot;DAILY_US&quot; |
| HOLD | &quot;HOLD&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| WEEKLY_MON_TO_FRI_AU | &quot;WEEKLY_MON_TO_FRI_AU&quot; |
| WEEKLY_MON_TO_FRI_EU | &quot;WEEKLY_MON_TO_FRI_EU&quot; |
| WEEKLY_MON_TO_FRI_US | &quot;WEEKLY_MON_TO_FRI_US&quot; |
| WEEKLY_ON_TUE_FRI_MIDNIGHT | &quot;WEEKLY_ON_TUE_FRI_MIDNIGHT&quot; |
| WEEKLY_SUN_TO_THU_AU | &quot;WEEKLY_SUN_TO_THU_AU&quot; |
| WEEKLY_SUN_TO_THU_US | &quot;WEEKLY_SUN_TO_THU_US&quot; |



