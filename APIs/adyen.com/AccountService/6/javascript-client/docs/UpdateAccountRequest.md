# AccountApi.UpdateAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | The code of the account to update. | 
**bankAccountUUID** | **String** | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. | [optional] 
**description** | **String** | A description of the account, maximum 256 characters.You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores &#x60;_&#x60;. | [optional] 
**metadata** | **{String: String}** | A set of key and value pairs for general use by the merchant. The keys do not have specific names and may be used for storing miscellaneous data as desired. &gt; Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. | [optional] 
**payoutMethodCode** | **String** | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. | [optional] 
**payoutSchedule** | [**UpdatePayoutScheduleRequest**](UpdatePayoutScheduleRequest.md) | The details of the payout schedule, to which the account should be updated. | [optional] 
**payoutSpeed** | **String** | Speed with which payouts for this account are processed. Permitted values: &#x60;STANDARD&#x60;, &#x60;SAME_DAY&#x60;. | [optional] 



## Enum: PayoutSpeedEnum


* `INSTANT` (value: `"INSTANT"`)

* `SAME_DAY` (value: `"SAME_DAY"`)

* `STANDARD` (value: `"STANDARD"`)




