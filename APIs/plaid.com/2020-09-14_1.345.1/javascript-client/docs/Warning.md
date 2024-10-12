# ThePlaidApi.Warning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | [**Cause**](Cause.md) |  | 
**warningCode** | **String** | The warning code identifies a specific kind of warning. &#x60;OWNERS_UNAVAILABLE&#x60; indicates that account-owner information is not available.&#x60;INVESTMENTS_UNAVAILABLE&#x60; indicates that Investments specific information is not available. &#x60;TRANSACTIONS_UNAVAILABLE&#x60; indicates that transactions information associated with Credit and Depository accounts are unavailable. | 
**warningType** | **String** | The warning type, which will always be &#x60;ASSET_REPORT_WARNING&#x60; | 



## Enum: WarningCodeEnum


* `OWNERS_UNAVAILABLE` (value: `"OWNERS_UNAVAILABLE"`)

* `INVESTMENTS_UNAVAILABLE` (value: `"INVESTMENTS_UNAVAILABLE"`)

* `TRANSACTIONS_UNAVAILABLE` (value: `"TRANSACTIONS_UNAVAILABLE"`)




