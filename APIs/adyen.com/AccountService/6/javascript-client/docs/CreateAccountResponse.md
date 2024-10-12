# AccountApi.CreateAccountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | The code of the new account. | [optional] 
**accountHolderCode** | **String** | The code of the account holder. | [optional] 
**bankAccountUUID** | **String** | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. | [optional] 
**description** | **String** | The description of the account. | [optional] 
**invalidFields** | [**[ErrorFieldType]**](ErrorFieldType.md) | A list of fields that caused the &#x60;/createAccount&#x60; request to fail. | [optional] 
**metadata** | **{String: String}** | A set of key and value pairs containing metadata. | [optional] 
**payoutMethodCode** | **String** | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. | [optional] 
**payoutSchedule** | [**PayoutScheduleResponse**](PayoutScheduleResponse.md) | The payout schedule of the account. | [optional] 
**payoutSpeed** | **String** | Speed with which payouts for this account are processed. Permitted values: &#x60;STANDARD&#x60;, &#x60;SAME_DAY&#x60;. | [optional] 
**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. | [optional] 
**resultCode** | **String** | The result code. | [optional] 
**status** | **String** | The status of the account. &gt;Permitted values: &#x60;Active&#x60;. | [optional] 



## Enum: PayoutSpeedEnum


* `INSTANT` (value: `"INSTANT"`)

* `SAME_DAY` (value: `"SAME_DAY"`)

* `STANDARD` (value: `"STANDARD"`)





## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Closed` (value: `"Closed"`)

* `Inactive` (value: `"Inactive"`)

* `Suspended` (value: `"Suspended"`)




