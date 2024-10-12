

# CreateAccountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of Account Holder under which to create the account. |  |
|**description** | **String** | A description of the account, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores &#x60;_&#x60;. |  [optional] |
|**payoutSchedule** | [**PayoutScheduleEnum**](#PayoutScheduleEnum) | The payout schedule of the prospective account. &gt;Permitted values: &#x60;DEFAULT&#x60;, &#x60;HOLD&#x60;, &#x60;DAILY&#x60;, &#x60;WEEKLY&#x60;, &#x60;MONTHLY&#x60;. |  [optional] |
|**payoutScheduleReason** | **String** | The reason for the payout schedule choice. &gt;Required if the payoutSchedule is &#x60;HOLD&#x60;. |  [optional] |



## Enum: PayoutScheduleEnum

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



