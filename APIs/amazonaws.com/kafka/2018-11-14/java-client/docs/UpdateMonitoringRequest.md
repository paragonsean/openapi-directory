

# UpdateMonitoringRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentVersion** | **String** |              &lt;p&gt;The version of the MSK cluster to update. Cluster versions aren&#39;t simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.&lt;/p&gt;           |  |
|**enhancedMonitoring** | [**EnhancedMonitoringEnum**](#EnhancedMonitoringEnum) |              &lt;p&gt;Specifies which metrics are gathered for the MSK cluster. This property has the following possible values: DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION. For a list of the metrics associated with each of these levels of monitoring, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html\&quot;&gt;Monitoring&lt;/a&gt;.&lt;/p&gt;           |  [optional] |
|**openMonitoring** | [**CreateClusterRequestOpenMonitoring**](CreateClusterRequestOpenMonitoring.md) |  |  [optional] |
|**loggingInfo** | [**CreateClusterRequestLoggingInfo**](CreateClusterRequestLoggingInfo.md) |  |  [optional] |



## Enum: EnhancedMonitoringEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| PER_BROKER | &quot;PER_BROKER&quot; |
| PER_TOPIC_PER_BROKER | &quot;PER_TOPIC_PER_BROKER&quot; |
| PER_TOPIC_PER_PARTITION | &quot;PER_TOPIC_PER_PARTITION&quot; |



