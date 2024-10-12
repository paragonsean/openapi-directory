

# WorkerMessageResponse

A worker_message response allows the server to pass information to the sender.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**streamingScalingReportResponse** | [**StreamingScalingReportResponse**](StreamingScalingReportResponse.md) |  |  [optional] |
|**workerHealthReportResponse** | [**WorkerHealthReportResponse**](WorkerHealthReportResponse.md) |  |  [optional] |
|**workerMetricsResponse** | **Object** | Service-side response to WorkerMessage reporting resource utilization. |  [optional] |
|**workerShutdownNoticeResponse** | **Object** | Service-side response to WorkerMessage issuing shutdown notice. |  [optional] |
|**workerThreadScalingReportResponse** | [**WorkerThreadScalingReportResponse**](WorkerThreadScalingReportResponse.md) |  |  [optional] |



