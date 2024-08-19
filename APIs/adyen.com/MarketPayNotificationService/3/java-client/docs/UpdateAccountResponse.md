

# UpdateAccountResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | The code of the account. |  |
|**payoutSchedule** | [**PayoutScheduleResponse**](PayoutScheduleResponse.md) | The payout schedule of the account. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |
|**submittedAsync** | **Boolean** | Indicates whether the request is processed asynchronously. Depending on the request&#39;s platform settings, the following scenarios may be applied: * **true**: The request is queued and will be executed when the providing service is available in the order in which the requests are received. * **false**: The processing of the request is immediately attempted; it may result in an error if the providing service is unavailable. |  [optional] |



