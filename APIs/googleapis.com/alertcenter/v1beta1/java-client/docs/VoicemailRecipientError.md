

# VoicemailRecipientError

Issue(s) with a voicemail recipient.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Email address of the invalid recipient. This may be unavailable if the recipient was deleted. |  [optional] |
|**invalidReason** | [**InvalidReasonEnum**](#InvalidReasonEnum) | Reason for the error. |  [optional] |



## Enum: InvalidReasonEnum

| Name | Value |
|---- | -----|
| EMAIL_INVALID_REASON_UNSPECIFIED | &quot;EMAIL_INVALID_REASON_UNSPECIFIED&quot; |
| OUT_OF_QUOTA | &quot;OUT_OF_QUOTA&quot; |
| RECIPIENT_DELETED | &quot;RECIPIENT_DELETED&quot; |



