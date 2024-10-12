

# OperationMetadata

OperationMetadata provides information about the operation execution. Returned in the long-running operation's metadata field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiMethodName** | **String** | The name of the API method that initiated the operation. |  [optional] |
|**cancelRequested** | **Boolean** | Specifies if cancellation was requested for the operation. |  [optional] |
|**counter** | [**ProgressCounter**](ProgressCounter.md) |  |  [optional] |
|**createTime** | **String** | The time at which the operation was created by the API. |  [optional] |
|**endTime** | **String** | The time at which execution workloads were completed. Some tasks will complete after this time such as logging audit logs. |  [optional] |
|**logsUrl** | **String** | A link to audit and error logs in the log viewer. Error logs are generated only by some operations, listed at [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). The &#x60;end_time&#x60; specified in this URL may not match the end time on the metadata because logs are written asynchronously from execution. |  [optional] |



