# CloudDataprocApi.Metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricOverrides** | **[String]** | Optional. Specify one or more Custom metrics (https://cloud.google.com/dataproc/docs/guides/dataproc-metrics#custom_metrics) to collect for the metric course (for the SPARK metric source (any Spark metric (https://spark.apache.org/docs/latest/monitoring.html#metrics) can be specified).Provide metrics in the following format: METRIC_SOURCE: INSTANCE:GROUP:METRIC Use camelcase as appropriate.Examples: yarn:ResourceManager:QueueMetrics:AppsCompleted spark:driver:DAGScheduler:job.allJobs sparkHistoryServer:JVM:Memory:NonHeapMemoryUsage.committed hiveserver2:JVM:Memory:NonHeapMemoryUsage.used Notes: Only the specified overridden metrics are collected for the metric source. For example, if one or more spark:executive metrics are listed as metric overrides, other SPARK metrics are not collected. The collection of the metrics for other enabled custom metric sources is unaffected. For example, if both SPARK andd YARN metric sources are enabled, and overrides are provided for Spark metrics only, all YARN metrics are collected. | [optional] 
**metricSource** | **String** | Required. A standard set of metrics is collected unless metricOverrides are specified for the metric source (see Custom metrics (https://cloud.google.com/dataproc/docs/guides/dataproc-metrics#custom_metrics) for more information). | [optional] 



## Enum: MetricSourceEnum


* `METRIC_SOURCE_UNSPECIFIED` (value: `"METRIC_SOURCE_UNSPECIFIED"`)

* `MONITORING_AGENT_DEFAULTS` (value: `"MONITORING_AGENT_DEFAULTS"`)

* `HDFS` (value: `"HDFS"`)

* `SPARK` (value: `"SPARK"`)

* `YARN` (value: `"YARN"`)

* `SPARK_HISTORY_SERVER` (value: `"SPARK_HISTORY_SERVER"`)

* `HIVESERVER2` (value: `"HIVESERVER2"`)

* `HIVEMETASTORE` (value: `"HIVEMETASTORE"`)

* `FLINK` (value: `"FLINK"`)




