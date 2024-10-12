# CloudSqlAdminApi.InsightsConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queryInsightsEnabled** | **Boolean** | Whether Query Insights feature is enabled. | [optional] 
**queryPlansPerMinute** | **Number** | Number of query execution plans captured by Insights per minute for all queries combined. Default is 5. | [optional] 
**queryStringLength** | **Number** | Maximum query length stored in bytes. Default value: 1024 bytes. Range: 256-4500 bytes. Query length more than this field value will be truncated to this value. When unset, query length will be the default value. Changing query length will restart the database. | [optional] 
**recordApplicationTags** | **Boolean** | Whether Query Insights will record application tags from query when enabled. | [optional] 
**recordClientAddress** | **Boolean** | Whether Query Insights will record client address when enabled. | [optional] 


