

# PullRequest

Request for the Pull method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**returnImmediately** | **Boolean** | If this is specified as true the system will respond immediately even if it is not able to return a message in the Pull response. Otherwise the system is allowed to wait until at least one message is available rather than returning FAILED_PRECONDITION. The client may cancel the request if it does not wish to wait any longer for the response. |  [optional] |
|**subscription** | **String** | The subscription from which a message should be pulled. |  [optional] |



