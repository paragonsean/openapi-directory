

# UpdateAccountResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | The code of the account. |  |
|**bankAccountUUID** | **String** | The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder. |  [optional] |
|**description** | **String** | The description of the account. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | A list of fields that caused the &#x60;/updateAccount&#x60; request to fail. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | A set of key and value pairs containing metadata. |  [optional] |
|**payoutMethodCode** | **String** | The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code. |  [optional] |
|**payoutSchedule** | [**PayoutScheduleResponse**](PayoutScheduleResponse.md) | The payout schedule of the account. |  [optional] |
|**payoutSpeed** | [**PayoutSpeedEnum**](#PayoutSpeedEnum) | Speed with which payouts for this account are processed. Permitted values: &#x60;STANDARD&#x60;, &#x60;SAME_DAY&#x60;. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |



## Enum: PayoutSpeedEnum

| Name | Value |
|---- | -----|
| INSTANT | &quot;INSTANT&quot; |
| SAME_DAY | &quot;SAME_DAY&quot; |
| STANDARD | &quot;STANDARD&quot; |



