

# PullRequest

Request for the `Pull` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxMessages** | **Integer** | The maximum number of messages returned for this request. The Pub/Sub system may return fewer than the number specified. |  [optional] |
|**returnImmediately** | **Boolean** | Optional. If this is specified as true the system will respond immediately even if it is not able to return a message in the &#x60;Pull&#x60; response. Otherwise the system is allowed to wait until at least one message is available rather than returning no messages. The client may cancel the request if it does not wish to wait any longer for the response. Warning: setting this field to &#x60;true&#x60; is discouraged because it adversely impacts the performance of &#x60;Pull&#x60; operations. We recommend that users do not set this field. |  [optional] |



