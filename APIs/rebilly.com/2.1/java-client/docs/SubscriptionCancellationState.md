

# SubscriptionCancellationState


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancelCategory** | [**CancelCategoryEnum**](#CancelCategoryEnum) | Cancel category. |  [optional] [readonly] |
|**cancelDescription** | **String** | Cancel reason description in free form. |  [optional] [readonly] |
|**canceledBy** | [**CanceledByEnum**](#CanceledByEnum) | Canceled by. |  [optional] [readonly] |
|**canceledTime** | **OffsetDateTime** | Subscription order canceled time. |  [optional] [readonly] |



## Enum: CancelCategoryEnum

| Name | Value |
|---- | -----|
| BILLING_FAILURE | &quot;billing-failure&quot; |
| DID_NOT_USE | &quot;did-not-use&quot; |
| DID_NOT_WANT | &quot;did-not-want&quot; |
| MISSING_FEATURES | &quot;missing-features&quot; |
| BUGS_OR_PROBLEMS | &quot;bugs-or-problems&quot; |
| DO_NOT_REMEMBER | &quot;do-not-remember&quot; |
| RISK_WARNING | &quot;risk-warning&quot; |
| CONTRACT_EXPIRED | &quot;contract-expired&quot; |
| TOO_EXPENSIVE | &quot;too-expensive&quot; |
| NEVER_STARTED | &quot;never-started&quot; |
| SWITCHED_PLAN | &quot;switched-plan&quot; |
| OTHER | &quot;other&quot; |



## Enum: CanceledByEnum

| Name | Value |
|---- | -----|
| MERCHANT | &quot;merchant&quot; |
| CUSTOMER | &quot;customer&quot; |
| REBILLY | &quot;rebilly&quot; |



