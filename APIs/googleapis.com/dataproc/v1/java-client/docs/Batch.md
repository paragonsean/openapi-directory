

# Batch

A representation of a batch workload in the service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the batch was created. |  [optional] [readonly] |
|**creator** | **String** | Output only. The email address of the user who created the batch. |  [optional] [readonly] |
|**environmentConfig** | [**EnvironmentConfig**](EnvironmentConfig.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels to associate with this batch. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a batch. |  [optional] |
|**name** | **String** | Output only. The resource name of the batch. |  [optional] [readonly] |
|**operation** | **String** | Output only. The resource name of the operation associated with this batch. |  [optional] [readonly] |
|**pysparkBatch** | [**PySparkBatch**](PySparkBatch.md) |  |  [optional] |
|**runtimeConfig** | [**RuntimeConfig**](RuntimeConfig.md) |  |  [optional] |
|**runtimeInfo** | [**RuntimeInfo**](RuntimeInfo.md) |  |  [optional] |
|**sparkBatch** | [**SparkBatch**](SparkBatch.md) |  |  [optional] |
|**sparkRBatch** | [**SparkRBatch**](SparkRBatch.md) |  |  [optional] |
|**sparkSqlBatch** | [**SparkSqlBatch**](SparkSqlBatch.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the batch. |  [optional] [readonly] |
|**stateHistory** | [**List&lt;StateHistory&gt;**](StateHistory.md) | Output only. Historical state information for the batch. |  [optional] [readonly] |
|**stateMessage** | **String** | Output only. Batch state details, such as a failure description if the state is FAILED. |  [optional] [readonly] |
|**stateTime** | **String** | Output only. The time when the batch entered a current state. |  [optional] [readonly] |
|**uuid** | **String** | Output only. A batch UUID (Unique Universal Identifier). The service generates this value when it creates the batch. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



