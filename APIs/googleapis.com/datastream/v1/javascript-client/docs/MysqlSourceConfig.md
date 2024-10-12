# DatastreamApi.MysqlSourceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludeObjects** | [**MysqlRdbms**](MysqlRdbms.md) |  | [optional] 
**includeObjects** | [**MysqlRdbms**](MysqlRdbms.md) |  | [optional] 
**maxConcurrentBackfillTasks** | **Number** | Maximum number of concurrent backfill tasks. The number should be non negative. If not set (or set to 0), the system&#39;s default value will be used. | [optional] 
**maxConcurrentCdcTasks** | **Number** | Maximum number of concurrent CDC tasks. The number should be non negative. If not set (or set to 0), the system&#39;s default value will be used. | [optional] 


