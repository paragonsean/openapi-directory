

# IssuesLockRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lockReason** | [**LockReasonEnum**](#LockReasonEnum) | The reason for locking the issue or pull request conversation. Lock will fail if you don&#39;t use one of these reasons:    * &#x60;off-topic&#x60;    * &#x60;too heated&#x60;    * &#x60;resolved&#x60;    * &#x60;spam&#x60; |  [optional] |



## Enum: LockReasonEnum

| Name | Value |
|---- | -----|
| OFF_TOPIC | &quot;off-topic&quot; |
| TOO_HEATED | &quot;too heated&quot; |
| RESOLVED | &quot;resolved&quot; |
| SPAM | &quot;spam&quot; |



