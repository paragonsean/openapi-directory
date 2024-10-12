# CloudLoggingApi.BigQueryOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usePartitionedTables** | **Boolean** | Optional. Whether to use BigQuery&#39;s partition tables (https://cloud.google.com/bigquery/docs/partitioned-tables). By default, Cloud Logging creates dated tables based on the log entries&#39; timestamps, e.g. syslog_20170523. With partitioned tables the date suffix is no longer present and special query syntax (https://cloud.google.com/bigquery/docs/querying-partitioned-tables) has to be used instead. In both cases, tables are sharded based on UTC timezone. | [optional] 
**usesTimestampColumnPartitioning** | **Boolean** | Output only. True if new timestamp column based partitioning is in use, false if legacy ingress-time partitioning is in use.All new sinks will have this field set true and will use timestamp column based partitioning. If use_partitioned_tables is false, this value has no meaning and will be false. Legacy sinks using partitioned tables will have this field set to false. | [optional] [readonly] 


