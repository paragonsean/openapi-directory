# AccountApi.AccountHolderStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**[AccountEventWrapper]**](AccountEventWrapper.md) | A list of events scheduled for the account holder. | [optional] 
**payoutState** | [**AccountPayoutState**](AccountPayoutState.md) | The payout state of the account holder. | [optional] 
**processingState** | [**AccountProcessingState**](AccountProcessingState.md) | The processing state of the account holder. | [optional] 
**status** | **String** | The status of the account holder. &gt;Permitted values: &#x60;Active&#x60;, &#x60;Inactive&#x60;, &#x60;Suspended&#x60;, &#x60;Closed&#x60;. | 
**statusReason** | **String** | The reason why the status was assigned to the account holder. | [optional] 



## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Closed` (value: `"Closed"`)

* `Inactive` (value: `"Inactive"`)

* `Suspended` (value: `"Suspended"`)




