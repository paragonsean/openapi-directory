

# GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails

Describes the details of a cancelled or cancelling subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | [**ReasonEnum**](#ReasonEnum) | Output only. The reason of the cancellation. |  [optional] [readonly] |



## Enum: ReasonEnum

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



