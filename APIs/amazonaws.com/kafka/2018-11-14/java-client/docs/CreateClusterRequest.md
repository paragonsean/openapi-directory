

# CreateClusterRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brokerNodeGroupInfo** | [**CreateClusterRequestBrokerNodeGroupInfo**](CreateClusterRequestBrokerNodeGroupInfo.md) |  |  |
|**clientAuthentication** | [**CreateClusterRequestClientAuthentication**](CreateClusterRequestClientAuthentication.md) |  |  [optional] |
|**clusterName** | **String** |              &lt;p&gt;The name of the cluster.&lt;/p&gt;           |  |
|**configurationInfo** | [**CreateClusterRequestConfigurationInfo**](CreateClusterRequestConfigurationInfo.md) |  |  [optional] |
|**encryptionInfo** | [**CreateClusterRequestEncryptionInfo**](CreateClusterRequestEncryptionInfo.md) |  |  [optional] |
|**enhancedMonitoring** | [**EnhancedMonitoringEnum**](#EnhancedMonitoringEnum) |              &lt;p&gt;Specifies which metrics are gathered for the MSK cluster. This property has the following possible values: DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION. For a list of the metrics associated with each of these levels of monitoring, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html\&quot;&gt;Monitoring&lt;/a&gt;.&lt;/p&gt;           |  [optional] |
|**openMonitoring** | [**CreateClusterRequestOpenMonitoring**](CreateClusterRequestOpenMonitoring.md) |  |  [optional] |
|**kafkaVersion** | **String** |              &lt;p&gt;The version of Apache Kafka.&lt;/p&gt;           |  |
|**loggingInfo** | [**CreateClusterRequestLoggingInfo**](CreateClusterRequestLoggingInfo.md) |  |  [optional] |
|**numberOfBrokerNodes** | **Integer** |              &lt;p&gt;The number of broker nodes in the cluster.&lt;/p&gt;           |  |
|**tags** | **Map&lt;String, String&gt;** |              &lt;p&gt;Create tags when creating the cluster.&lt;/p&gt;           |  [optional] |
|**storageMode** | [**StorageModeEnum**](#StorageModeEnum) | Controls storage mode for various supported storage tiers. |  [optional] |



## Enum: EnhancedMonitoringEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| PER_BROKER | &quot;PER_BROKER&quot; |
| PER_TOPIC_PER_BROKER | &quot;PER_TOPIC_PER_BROKER&quot; |
| PER_TOPIC_PER_PARTITION | &quot;PER_TOPIC_PER_PARTITION&quot; |



## Enum: StorageModeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;LOCAL&quot; |
| TIERED | &quot;TIERED&quot; |



