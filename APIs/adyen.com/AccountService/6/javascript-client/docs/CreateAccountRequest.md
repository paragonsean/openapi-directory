# AccountApi.CreateAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of Account Holder under which to create the account. | 
**bankAccountUUID** | **String** | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. | [optional] 
**description** | **String** | A description of the account, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores &#x60;_&#x60;. | [optional] 
**metadata** | **{String: String}** | A set of key and value pairs for general use by the merchant. The keys do not have specific names and may be used for storing miscellaneous data as desired. &gt; Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. | [optional] 
**payoutMethodCode** | **String** | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. | [optional] 
**payoutSchedule** | **String** | The payout schedule of the prospective account. &gt;Permitted values: &#x60;DEFAULT&#x60;, &#x60;HOLD&#x60;, &#x60;DAILY&#x60;, &#x60;WEEKLY&#x60;, &#x60;MONTHLY&#x60;. | [optional] 
**payoutScheduleReason** | **String** | The reason for the payout schedule choice. &gt;Required if the payoutSchedule is &#x60;HOLD&#x60;. | [optional] 
**payoutSpeed** | **String** | Speed with which payouts for this account are processed. Permitted values: &#x60;STANDARD&#x60;, &#x60;SAME_DAY&#x60;. | [optional] [default to &#39;STANDARD&#39;]



## Enum: PayoutScheduleEnum


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





## Enum: PayoutSpeedEnum


* `INSTANT` (value: `"INSTANT"`)

* `SAME_DAY` (value: `"SAME_DAY"`)

* `STANDARD` (value: `"STANDARD"`)




