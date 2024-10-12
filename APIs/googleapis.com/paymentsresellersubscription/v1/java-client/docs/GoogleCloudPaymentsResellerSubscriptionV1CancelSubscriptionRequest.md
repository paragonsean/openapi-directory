

# GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest

Request to cancel a subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancelImmediately** | **Boolean** | Optional. If true, Google will cancel the subscription immediately, and may or may not (based on the contract) issue a prorated refund for the remainder of the billing cycle. Otherwise, Google defers the cancelation at renewal_time, and will not issue a refund. |  [optional] |
|**cancellationReason** | [**CancellationReasonEnum**](#CancellationReasonEnum) | Specifies the reason for the cancellation. |  [optional] |



## Enum: CancellationReasonEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CANCELLATION_REASON_UNSPECIFIED&quot; |
| FRAUD | &quot;CANCELLATION_REASON_FRAUD&quot; |
| REMORSE | &quot;CANCELLATION_REASON_REMORSE&quot; |
| ACCIDENTAL_PURCHASE | &quot;CANCELLATION_REASON_ACCIDENTAL_PURCHASE&quot; |
| PAST_DUE | &quot;CANCELLATION_REASON_PAST_DUE&quot; |
| ACCOUNT_CLOSED | &quot;CANCELLATION_REASON_ACCOUNT_CLOSED&quot; |
| UPGRADE_DOWNGRADE | &quot;CANCELLATION_REASON_UPGRADE_DOWNGRADE&quot; |
| USER_DELINQUENCY | &quot;CANCELLATION_REASON_USER_DELINQUENCY&quot; |
| SYSTEM_ERROR | &quot;CANCELLATION_REASON_SYSTEM_ERROR&quot; |
| SYSTEM_CANCEL | &quot;CANCELLATION_REASON_SYSTEM_CANCEL&quot; |
| OTHER | &quot;CANCELLATION_REASON_OTHER&quot; |



