

# CheckInRequest

The parameters to the CheckIn method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deadlineExpired** | **Object** | A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } |  [optional] |
|**event** | **Map&lt;String, Object&gt;** | A workflow specific event occurred. |  [optional] |
|**events** | [**List&lt;TimestampedEvent&gt;**](TimestampedEvent.md) | A list of timestamped events. |  [optional] |
|**result** | [**Status**](Status.md) |  |  [optional] |
|**sosReport** | **byte[]** | An SOS report for an unexpected VM failure. |  [optional] |
|**workerStatus** | [**WorkerStatus**](WorkerStatus.md) |  |  [optional] |



