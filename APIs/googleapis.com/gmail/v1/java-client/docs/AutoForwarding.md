

# AutoForwarding

Auto-forwarding settings for an account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disposition** | [**DispositionEnum**](#DispositionEnum) | The state that a message should be left in after it has been forwarded. |  [optional] |
|**emailAddress** | **String** | Email address to which all incoming messages are forwarded. This email address must be a verified member of the forwarding addresses. |  [optional] |
|**enabled** | **Boolean** | Whether all incoming mail is automatically forwarded to another address. |  [optional] |



## Enum: DispositionEnum

| Name | Value |
|---- | -----|
| DISPOSITION_UNSPECIFIED | &quot;dispositionUnspecified&quot; |
| LEAVE_IN_INBOX | &quot;leaveInInbox&quot; |
| ARCHIVE | &quot;archive&quot; |
| TRASH | &quot;trash&quot; |
| MARK_READ | &quot;markRead&quot; |



