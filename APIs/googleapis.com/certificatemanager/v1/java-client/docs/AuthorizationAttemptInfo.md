

# AuthorizationAttemptInfo

State of the latest attempt to authorize a domain for certificate issuance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Output only. Human readable explanation for reaching the state. Provided to help address the configuration issues. Not guaranteed to be stable. For programmatic access use FailureReason enum. |  [optional] [readonly] |
|**domain** | **String** | Domain name of the authorization attempt. |  [optional] |
|**failureReason** | [**FailureReasonEnum**](#FailureReasonEnum) | Output only. Reason for failure of the authorization attempt for the domain. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the domain for managed certificate issuance. |  [optional] [readonly] |



## Enum: FailureReasonEnum

| Name | Value |
|---- | -----|
| FAILURE_REASON_UNSPECIFIED | &quot;FAILURE_REASON_UNSPECIFIED&quot; |
| CONFIG | &quot;CONFIG&quot; |
| CAA | &quot;CAA&quot; |
| RATE_LIMITED | &quot;RATE_LIMITED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| AUTHORIZING | &quot;AUTHORIZING&quot; |
| AUTHORIZED | &quot;AUTHORIZED&quot; |
| FAILED | &quot;FAILED&quot; |



