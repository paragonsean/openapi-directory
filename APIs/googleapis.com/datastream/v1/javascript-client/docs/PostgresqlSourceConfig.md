# DatastreamApi.PostgresqlSourceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludeObjects** | [**PostgresqlRdbms**](PostgresqlRdbms.md) |  | [optional] 
**includeObjects** | [**PostgresqlRdbms**](PostgresqlRdbms.md) |  | [optional] 
**maxConcurrentBackfillTasks** | **Number** | Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system&#39;s default value will be used. | [optional] 
**publication** | **String** | Required. The name of the publication that includes the set of all tables that are defined in the stream&#39;s include_objects. | [optional] 
**replicationSlot** | **String** | Required. Immutable. The name of the logical replication slot that&#39;s configured with the pgoutput plugin. | [optional] 


