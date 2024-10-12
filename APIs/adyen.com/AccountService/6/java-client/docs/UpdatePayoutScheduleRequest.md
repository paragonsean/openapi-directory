

# UpdatePayoutScheduleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Direction on how to handle any payouts that have already been scheduled. Permitted values: * &#x60;CLOSE&#x60; will close the existing batch of payouts. * &#x60;UPDATE&#x60; will reschedule the existing batch to the new schedule. * &#x60;NOTHING&#x60; (**default**) will allow the payout to proceed. |  [optional] |
|**reason** | **String** | The reason for the payout schedule update. &gt; This field is required when the &#x60;schedule&#x60; parameter is set to &#x60;HOLD&#x60;. |  [optional] |
|**schedule** | [**ScheduleEnum**](#ScheduleEnum) | The payout schedule to which the account is to be updated. Permitted values: &#x60;DAILY&#x60;, &#x60;DAILY_US&#x60;, &#x60;DAILY_EU&#x60;, &#x60;DAILY_AU&#x60;, &#x60;DAILY_SG&#x60;, &#x60;WEEKLY&#x60;, &#x60;WEEKLY_ON_TUE_FRI_MIDNIGHT&#x60;, &#x60;BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT&#x60;, &#x60;MONTHLY&#x60;, &#x60;HOLD&#x60;. &#x60;HOLD&#x60; will prevent scheduled payouts from happening but will still allow manual payouts to occur. |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| CLOSE | &quot;CLOSE&quot; |
| NOTHING | &quot;NOTHING&quot; |
| UPDATE | &quot;UPDATE&quot; |



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



