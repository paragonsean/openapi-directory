# BigQueryDataTransferApi.DataSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationType** | **String** | Indicates the type of authorization. | [optional] 
**clientId** | **String** | Data source client id which should be used to receive refresh token. | [optional] 
**dataRefreshType** | **String** | Specifies whether the data source supports automatic data refresh for the past few days, and how it&#39;s supported. For some data sources, data might not be complete until a few days later, so it&#39;s useful to refresh data automatically. | [optional] 
**dataSourceId** | **String** | Data source id. | [optional] 
**defaultDataRefreshWindowDays** | **Number** | Default data refresh window on days. Only meaningful when &#x60;data_refresh_type&#x60; &#x3D; &#x60;SLIDING_WINDOW&#x60;. | [optional] 
**defaultSchedule** | **String** | Default data transfer schedule. Examples of valid schedules include: &#x60;1st,3rd monday of month 15:30&#x60;, &#x60;every wed,fri of jan,jun 13:15&#x60;, and &#x60;first sunday of quarter 00:00&#x60;. | [optional] 
**description** | **String** | User friendly data source description string. | [optional] 
**displayName** | **String** | User friendly data source name. | [optional] 
**helpUrl** | **String** | Url for the help document for this data source. | [optional] 
**manualRunsDisabled** | **Boolean** | Disables backfilling and manual run scheduling for the data source. | [optional] 
**minimumScheduleInterval** | **String** | The minimum interval for scheduler to schedule runs. | [optional] 
**name** | **String** | Output only. Data source resource name. | [optional] [readonly] 
**parameters** | [**[DataSourceParameter]**](DataSourceParameter.md) | Data source parameters. | [optional] 
**scopes** | **[String]** | Api auth scopes for which refresh token needs to be obtained. These are scopes needed by a data source to prepare data and ingest them into BigQuery, e.g., https://www.googleapis.com/auth/bigquery | [optional] 
**supportsCustomSchedule** | **Boolean** | Specifies whether the data source supports a user defined schedule, or operates on the default schedule. When set to &#x60;true&#x60;, user can override default schedule. | [optional] 
**supportsMultipleTransfers** | **Boolean** | Deprecated. This field has no effect. | [optional] 
**transferType** | **String** | Deprecated. This field has no effect. | [optional] 
**updateDeadlineSeconds** | **Number** | The number of seconds to wait for an update from the data source before the Data Transfer Service marks the transfer as FAILED. | [optional] 



## Enum: AuthorizationTypeEnum


* `AUTHORIZATION_TYPE_UNSPECIFIED` (value: `"AUTHORIZATION_TYPE_UNSPECIFIED"`)

* `AUTHORIZATION_CODE` (value: `"AUTHORIZATION_CODE"`)

* `GOOGLE_PLUS_AUTHORIZATION_CODE` (value: `"GOOGLE_PLUS_AUTHORIZATION_CODE"`)

* `FIRST_PARTY_OAUTH` (value: `"FIRST_PARTY_OAUTH"`)





## Enum: DataRefreshTypeEnum


* `DATA_REFRESH_TYPE_UNSPECIFIED` (value: `"DATA_REFRESH_TYPE_UNSPECIFIED"`)

* `SLIDING_WINDOW` (value: `"SLIDING_WINDOW"`)

* `CUSTOM_SLIDING_WINDOW` (value: `"CUSTOM_SLIDING_WINDOW"`)





## Enum: TransferTypeEnum


* `TRANSFER_TYPE_UNSPECIFIED` (value: `"TRANSFER_TYPE_UNSPECIFIED"`)

* `BATCH` (value: `"BATCH"`)

* `STREAMING` (value: `"STREAMING"`)




