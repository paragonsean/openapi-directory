# AccountApi.UpdatePayoutScheduleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Direction on how to handle any payouts that have already been scheduled. Permitted values: * &#x60;CLOSE&#x60; will close the existing batch of payouts. * &#x60;UPDATE&#x60; will reschedule the existing batch to the new schedule. * &#x60;NOTHING&#x60; (**default**) will allow the payout to proceed. | [optional] 
**reason** | **String** | The reason for the payout schedule update. &gt; This field is required when the &#x60;schedule&#x60; parameter is set to &#x60;HOLD&#x60;. | [optional] 
**schedule** | **String** | The payout schedule to which the account is to be updated. Permitted values: &#x60;DAILY&#x60;, &#x60;DAILY_US&#x60;, &#x60;DAILY_EU&#x60;, &#x60;DAILY_AU&#x60;, &#x60;DAILY_SG&#x60;, &#x60;WEEKLY&#x60;, &#x60;WEEKLY_ON_TUE_FRI_MIDNIGHT&#x60;, &#x60;BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT&#x60;, &#x60;MONTHLY&#x60;, &#x60;HOLD&#x60;. &#x60;HOLD&#x60; will prevent scheduled payouts from happening but will still allow manual payouts to occur. | 



## Enum: ActionEnum


* `CLOSE` (value: `"CLOSE"`)

* `NOTHING` (value: `"NOTHING"`)

* `UPDATE` (value: `"UPDATE"`)





## Enum: ScheduleEnum


* `BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT` (value: `"BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT"`)

* `DAILY` (value: `"DAILY"`)

* `DAILY_AU` (value: `"DAILY_AU"`)

* `DAILY_EU` (value: `"DAILY_EU"`)

* `DAILY_SG` (value: `"DAILY_SG"`)

* `DAILY_US` (value: `"DAILY_US"`)

* `HOLD` (value: `"HOLD"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `WEEKLY_MON_TO_FRI_AU` (value: `"WEEKLY_MON_TO_FRI_AU"`)

* `WEEKLY_MON_TO_FRI_EU` (value: `"WEEKLY_MON_TO_FRI_EU"`)

* `WEEKLY_MON_TO_FRI_US` (value: `"WEEKLY_MON_TO_FRI_US"`)

* `WEEKLY_ON_TUE_FRI_MIDNIGHT` (value: `"WEEKLY_ON_TUE_FRI_MIDNIGHT"`)

* `WEEKLY_SUN_TO_THU_AU` (value: `"WEEKLY_SUN_TO_THU_AU"`)

* `WEEKLY_SUN_TO_THU_US` (value: `"WEEKLY_SUN_TO_THU_US"`)




