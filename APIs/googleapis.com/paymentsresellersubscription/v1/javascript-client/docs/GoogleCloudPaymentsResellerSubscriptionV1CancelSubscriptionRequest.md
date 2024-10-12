# PaymentsResellerSubscriptionApi.GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelImmediately** | **Boolean** | Optional. If true, Google will cancel the subscription immediately, and may or may not (based on the contract) issue a prorated refund for the remainder of the billing cycle. Otherwise, Google defers the cancelation at renewal_time, and will not issue a refund. | [optional] 
**cancellationReason** | **String** | Specifies the reason for the cancellation. | [optional] 



## Enum: CancellationReasonEnum


* `UNSPECIFIED` (value: `"CANCELLATION_REASON_UNSPECIFIED"`)

* `FRAUD` (value: `"CANCELLATION_REASON_FRAUD"`)

* `REMORSE` (value: `"CANCELLATION_REASON_REMORSE"`)

* `ACCIDENTAL_PURCHASE` (value: `"CANCELLATION_REASON_ACCIDENTAL_PURCHASE"`)

* `PAST_DUE` (value: `"CANCELLATION_REASON_PAST_DUE"`)

* `ACCOUNT_CLOSED` (value: `"CANCELLATION_REASON_ACCOUNT_CLOSED"`)

* `UPGRADE_DOWNGRADE` (value: `"CANCELLATION_REASON_UPGRADE_DOWNGRADE"`)

* `USER_DELINQUENCY` (value: `"CANCELLATION_REASON_USER_DELINQUENCY"`)

* `SYSTEM_ERROR` (value: `"CANCELLATION_REASON_SYSTEM_ERROR"`)

* `SYSTEM_CANCEL` (value: `"CANCELLATION_REASON_SYSTEM_CANCEL"`)

* `OTHER` (value: `"CANCELLATION_REASON_OTHER"`)




