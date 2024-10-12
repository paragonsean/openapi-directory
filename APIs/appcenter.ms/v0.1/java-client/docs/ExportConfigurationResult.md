

# ExportConfigurationResult

Export configuration result

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **String** | Creation time in ISO 8601 format |  |
|**exportConfiguration** | [**ExportConfigurationsList200ResponseValuesInnerExportConfiguration**](ExportConfigurationsList200ResponseValuesInnerExportConfiguration.md) |  |  [optional] |
|**exportEntities** | [**List&lt;ExportEntitiesEnum&gt;**](#List&lt;ExportEntitiesEnum&gt;) |  |  [optional] |
|**exportType** | [**ExportTypeEnum**](#ExportTypeEnum) | Target resource type of export configuration |  |
|**id** | **String** | Export configuration id |  |
|**lastRunTime** | **String** | Latest time in ISO 8601 format when export completed successfully |  [optional] |
|**resourceGroup** | **String** | resource group for the storage account/App Insights resource |  [optional] |
|**resourceName** | **String** | Storage accout or Appinsights resource name |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the export job |  |
|**stateInfo** | **String** | Additional information about export configuration state |  [optional] |



## Enum: List&lt;ExportEntitiesEnum&gt;

| Name | Value |
|---- | -----|
| CRASHES | &quot;crashes&quot; |
| ERRORS | &quot;errors&quot; |
| ATTACHMENTS | &quot;attachments&quot; |
| NO_LOGS | &quot;no_logs&quot; |



## Enum: ExportTypeEnum

| Name | Value |
|---- | -----|
| BLOB_STORAGE | &quot;BlobStorage&quot; |
| APP_INSIGHTS | &quot;AppInsights&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |
| PENDING | &quot;Pending&quot; |
| DELETED | &quot;Deleted&quot; |
| INVALID | &quot;Invalid&quot; |



