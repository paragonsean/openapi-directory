

# DataSource

Defines the properties and custom parameters for a data source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationType** | [**AuthorizationTypeEnum**](#AuthorizationTypeEnum) | Indicates the type of authorization. |  [optional] |
|**clientId** | **String** | Data source client id which should be used to receive refresh token. |  [optional] |
|**dataRefreshType** | [**DataRefreshTypeEnum**](#DataRefreshTypeEnum) | Specifies whether the data source supports automatic data refresh for the past few days, and how it&#39;s supported. For some data sources, data might not be complete until a few days later, so it&#39;s useful to refresh data automatically. |  [optional] |
|**dataSourceId** | **String** | Data source id. |  [optional] |
|**defaultDataRefreshWindowDays** | **Integer** | Default data refresh window on days. Only meaningful when &#x60;data_refresh_type&#x60; &#x3D; &#x60;SLIDING_WINDOW&#x60;. |  [optional] |
|**defaultSchedule** | **String** | Default data transfer schedule. Examples of valid schedules include: &#x60;1st,3rd monday of month 15:30&#x60;, &#x60;every wed,fri of jan,jun 13:15&#x60;, and &#x60;first sunday of quarter 00:00&#x60;. |  [optional] |
|**description** | **String** | User friendly data source description string. |  [optional] |
|**displayName** | **String** | User friendly data source name. |  [optional] |
|**helpUrl** | **String** | Url for the help document for this data source. |  [optional] |
|**manualRunsDisabled** | **Boolean** | Disables backfilling and manual run scheduling for the data source. |  [optional] |
|**minimumScheduleInterval** | **String** | The minimum interval for scheduler to schedule runs. |  [optional] |
|**name** | **String** | Output only. Data source resource name. |  [optional] [readonly] |
|**parameters** | [**List&lt;DataSourceParameter&gt;**](DataSourceParameter.md) | Data source parameters. |  [optional] |
|**scopes** | **List&lt;String&gt;** | Api auth scopes for which refresh token needs to be obtained. These are scopes needed by a data source to prepare data and ingest them into BigQuery, e.g., https://www.googleapis.com/auth/bigquery |  [optional] |
|**supportsCustomSchedule** | **Boolean** | Specifies whether the data source supports a user defined schedule, or operates on the default schedule. When set to &#x60;true&#x60;, user can override default schedule. |  [optional] |
|**supportsMultipleTransfers** | **Boolean** | Deprecated. This field has no effect. |  [optional] |
|**transferType** | [**TransferTypeEnum**](#TransferTypeEnum) | Deprecated. This field has no effect. |  [optional] |
|**updateDeadlineSeconds** | **Integer** | The number of seconds to wait for an update from the data source before the Data Transfer Service marks the transfer as FAILED. |  [optional] |



## Enum: AuthorizationTypeEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION_TYPE_UNSPECIFIED | &quot;AUTHORIZATION_TYPE_UNSPECIFIED&quot; |
| AUTHORIZATION_CODE | &quot;AUTHORIZATION_CODE&quot; |
| GOOGLE_PLUS_AUTHORIZATION_CODE | &quot;GOOGLE_PLUS_AUTHORIZATION_CODE&quot; |
| FIRST_PARTY_OAUTH | &quot;FIRST_PARTY_OAUTH&quot; |



## Enum: DataRefreshTypeEnum

| Name | Value |
|---- | -----|
| DATA_REFRESH_TYPE_UNSPECIFIED | &quot;DATA_REFRESH_TYPE_UNSPECIFIED&quot; |
| SLIDING_WINDOW | &quot;SLIDING_WINDOW&quot; |
| CUSTOM_SLIDING_WINDOW | &quot;CUSTOM_SLIDING_WINDOW&quot; |



## Enum: TransferTypeEnum

| Name | Value |
|---- | -----|
| TRANSFER_TYPE_UNSPECIFIED | &quot;TRANSFER_TYPE_UNSPECIFIED&quot; |
| BATCH | &quot;BATCH&quot; |
| STREAMING | &quot;STREAMING&quot; |



