

# WorkerMessage

WorkerMessage provides information to the backend about a worker.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSamplingReport** | [**DataSamplingReport**](DataSamplingReport.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels are used to group WorkerMessages. For example, a worker_message about a particular container might have the labels: { \&quot;JOB_ID\&quot;: \&quot;2015-04-22\&quot;, \&quot;WORKER_ID\&quot;: \&quot;wordcount-vm-2015…\&quot; \&quot;CONTAINER_TYPE\&quot;: \&quot;worker\&quot;, \&quot;CONTAINER_ID\&quot;: \&quot;ac1234def\&quot;} Label tags typically correspond to Label enum values. However, for ease of development other strings can be used as tags. LABEL_UNSPECIFIED should not be used here. |  [optional] |
|**perWorkerMetrics** | [**PerWorkerMetrics**](PerWorkerMetrics.md) |  |  [optional] |
|**streamingScalingReport** | [**StreamingScalingReport**](StreamingScalingReport.md) |  |  [optional] |
|**time** | **String** | The timestamp of the worker_message. |  [optional] |
|**workerHealthReport** | [**WorkerHealthReport**](WorkerHealthReport.md) |  |  [optional] |
|**workerLifecycleEvent** | [**WorkerLifecycleEvent**](WorkerLifecycleEvent.md) |  |  [optional] |
|**workerMessageCode** | [**WorkerMessageCode**](WorkerMessageCode.md) |  |  [optional] |
|**workerMetrics** | [**ResourceUtilizationReport**](ResourceUtilizationReport.md) |  |  [optional] |
|**workerShutdownNotice** | [**WorkerShutdownNotice**](WorkerShutdownNotice.md) |  |  [optional] |
|**workerThreadScalingReport** | [**WorkerThreadScalingReport**](WorkerThreadScalingReport.md) |  |  [optional] |



