

# PopSettings

POP settings for an account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessWindow** | [**AccessWindowEnum**](#AccessWindowEnum) | The range of messages which are accessible via POP. |  [optional] |
|**disposition** | [**DispositionEnum**](#DispositionEnum) | The action that will be executed on a message after it has been fetched via POP. |  [optional] |



## Enum: AccessWindowEnum

| Name | Value |
|---- | -----|
| ACCESS_WINDOW_UNSPECIFIED | &quot;accessWindowUnspecified&quot; |
| DISABLED | &quot;disabled&quot; |
| FROM_NOW_ON | &quot;fromNowOn&quot; |
| ALL_MAIL | &quot;allMail&quot; |



## Enum: DispositionEnum

| Name | Value |
|---- | -----|
| DISPOSITION_UNSPECIFIED | &quot;dispositionUnspecified&quot; |
| LEAVE_IN_INBOX | &quot;leaveInInbox&quot; |
| ARCHIVE | &quot;archive&quot; |
| TRASH | &quot;trash&quot; |
| MARK_READ | &quot;markRead&quot; |



