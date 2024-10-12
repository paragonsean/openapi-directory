

# Delegate

Settings for a delegate. Delegates can read, send, and delete messages, as well as view and add contacts, for the delegator's account. See \"Set up mail delegation\" for more information about delegates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delegateEmail** | **String** | The email address of the delegate. |  [optional] |
|**verificationStatus** | [**VerificationStatusEnum**](#VerificationStatusEnum) | Indicates whether this address has been verified and can act as a delegate for the account. Read-only. |  [optional] |



## Enum: VerificationStatusEnum

| Name | Value |
|---- | -----|
| VERIFICATION_STATUS_UNSPECIFIED | &quot;verificationStatusUnspecified&quot; |
| ACCEPTED | &quot;accepted&quot; |
| PENDING | &quot;pending&quot; |
| REJECTED | &quot;rejected&quot; |
| EXPIRED | &quot;expired&quot; |



