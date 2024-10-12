

# SoftwareConfig

Specifies the selection and config of software inside the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageVersion** | **String** | Optional. The version of software inside the cluster. It must be one of the supported Dataproc Versions (https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions), such as \&quot;1.2\&quot; (including a subminor version, such as \&quot;1.2.29\&quot;), or the \&quot;preview\&quot; version (https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#other_versions). If unspecified, it defaults to the latest Debian version. |  [optional] |
|**optionalComponents** | [**List&lt;OptionalComponentsEnum&gt;**](#List&lt;OptionalComponentsEnum&gt;) | Optional. The set of components to activate on the cluster. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. The properties to set on daemon config files.Property keys are specified in prefix:property format, for example core:hadoop.tmp.dir. The following are supported prefixes and their mappings: capacity-scheduler: capacity-scheduler.xml core: core-site.xml distcp: distcp-default.xml hdfs: hdfs-site.xml hive: hive-site.xml mapred: mapred-site.xml pig: pig.properties spark: spark-defaults.conf yarn: yarn-site.xmlFor more information, see Cluster properties (https://cloud.google.com/dataproc/docs/concepts/cluster-properties). |  [optional] |



## Enum: List&lt;OptionalComponentsEnum&gt;

| Name | Value |
|---- | -----|
| COMPONENT_UNSPECIFIED | &quot;COMPONENT_UNSPECIFIED&quot; |
| ANACONDA | &quot;ANACONDA&quot; |
| DOCKER | &quot;DOCKER&quot; |
| DRUID | &quot;DRUID&quot; |
| FLINK | &quot;FLINK&quot; |
| HBASE | &quot;HBASE&quot; |
| HIVE_WEBHCAT | &quot;HIVE_WEBHCAT&quot; |
| HUDI | &quot;HUDI&quot; |
| JUPYTER | &quot;JUPYTER&quot; |
| PRESTO | &quot;PRESTO&quot; |
| TRINO | &quot;TRINO&quot; |
| RANGER | &quot;RANGER&quot; |
| SOLR | &quot;SOLR&quot; |
| ZEPPELIN | &quot;ZEPPELIN&quot; |
| ZOOKEEPER | &quot;ZOOKEEPER&quot; |



