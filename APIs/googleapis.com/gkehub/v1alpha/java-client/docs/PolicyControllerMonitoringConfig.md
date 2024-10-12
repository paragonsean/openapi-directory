

# PolicyControllerMonitoringConfig

MonitoringConfig specifies the backends Policy Controller should export metrics to. For example, to specify metrics should be exported to Cloud Monitoring and Prometheus, specify backends: [\"cloudmonitoring\", \"prometheus\"]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backends** | [**List&lt;BackendsEnum&gt;**](#List&lt;BackendsEnum&gt;) | Specifies the list of backends Policy Controller will export to. An empty list would effectively disable metrics export. |  [optional] |



## Enum: List&lt;BackendsEnum&gt;

| Name | Value |
|---- | -----|
| MONITORING_BACKEND_UNSPECIFIED | &quot;MONITORING_BACKEND_UNSPECIFIED&quot; |
| PROMETHEUS | &quot;PROMETHEUS&quot; |
| CLOUD_MONITORING | &quot;CLOUD_MONITORING&quot; |



