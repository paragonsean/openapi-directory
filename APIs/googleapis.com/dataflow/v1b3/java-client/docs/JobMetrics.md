

# JobMetrics

JobMetrics contains a collection of metrics describing the detailed progress of a Dataflow job. Metrics correspond to user-defined and system-defined metrics in the job. For more information, see [Dataflow job metrics] (https://cloud.google.com/dataflow/docs/guides/using-monitoring-intf). This resource captures only the most recent values of each metric; time-series data can be queried for them (under the same metric names) from Cloud Monitoring.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricTime** | **String** | Timestamp as of which metric values are current. |  [optional] |
|**metrics** | [**List&lt;MetricUpdate&gt;**](MetricUpdate.md) | All metrics for this job. |  [optional] |



