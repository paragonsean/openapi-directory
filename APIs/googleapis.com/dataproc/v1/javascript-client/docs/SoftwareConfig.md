# CloudDataprocApi.SoftwareConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imageVersion** | **String** | Optional. The version of software inside the cluster. It must be one of the supported Dataproc Versions (https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_dataproc_versions), such as \&quot;1.2\&quot; (including a subminor version, such as \&quot;1.2.29\&quot;), or the \&quot;preview\&quot; version (https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#other_versions). If unspecified, it defaults to the latest Debian version. | [optional] 
**optionalComponents** | **[String]** | Optional. The set of components to activate on the cluster. | [optional] 
**properties** | **{String: String}** | Optional. The properties to set on daemon config files.Property keys are specified in prefix:property format, for example core:hadoop.tmp.dir. The following are supported prefixes and their mappings: capacity-scheduler: capacity-scheduler.xml core: core-site.xml distcp: distcp-default.xml hdfs: hdfs-site.xml hive: hive-site.xml mapred: mapred-site.xml pig: pig.properties spark: spark-defaults.conf yarn: yarn-site.xmlFor more information, see Cluster properties (https://cloud.google.com/dataproc/docs/concepts/cluster-properties). | [optional] 



## Enum: [OptionalComponentsEnum]


* `COMPONENT_UNSPECIFIED` (value: `"COMPONENT_UNSPECIFIED"`)

* `ANACONDA` (value: `"ANACONDA"`)

* `DOCKER` (value: `"DOCKER"`)

* `DRUID` (value: `"DRUID"`)

* `FLINK` (value: `"FLINK"`)

* `HBASE` (value: `"HBASE"`)

* `HIVE_WEBHCAT` (value: `"HIVE_WEBHCAT"`)

* `HUDI` (value: `"HUDI"`)

* `JUPYTER` (value: `"JUPYTER"`)

* `PRESTO` (value: `"PRESTO"`)

* `TRINO` (value: `"TRINO"`)

* `RANGER` (value: `"RANGER"`)

* `SOLR` (value: `"SOLR"`)

* `ZEPPELIN` (value: `"ZEPPELIN"`)

* `ZOOKEEPER` (value: `"ZOOKEEPER"`)




