# GoogleWorkspaceAlertCenterApi.AccountSuspensionWarning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appealWindow** | **String** | The amount of time remaining to appeal an imminent suspension. After this window has elapsed, the account will be suspended. Only populated if the account suspension is in WARNING state. | [optional] 
**state** | **String** | Account suspension warning state. | [optional] 
**suspensionDetails** | [**[AccountSuspensionDetails]**](AccountSuspensionDetails.md) | Details about why an account is being suspended. | [optional] 



## Enum: StateEnum


* `ACCOUNT_SUSPENSION_WARNING_STATE_UNSPECIFIED` (value: `"ACCOUNT_SUSPENSION_WARNING_STATE_UNSPECIFIED"`)

* `WARNING` (value: `"WARNING"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `APPEAL_APPROVED` (value: `"APPEAL_APPROVED"`)

* `APPEAL_SUBMITTED` (value: `"APPEAL_SUBMITTED"`)




