

# ExportConfigurationsList200ResponseValuesInnerExportConfiguration

Export configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backfill** | **Boolean** | Field to determine if backfilling should occur. The default value is true. If set to false export starts from date and time of config creation. |  [optional] |
|**exportEntities** | [**List&lt;ExportEntitiesEnum&gt;**](#List&lt;ExportEntitiesEnum&gt;) |  |  [optional] |
|**resourceGroup** | **String** | The resource group name on azure |  [optional] |
|**resourceName** | **String** | The resource name on azure |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of export configuration |  |



## Enum: List&lt;ExportEntitiesEnum&gt;

| Name | Value |
|---- | -----|
| CRASHES | &quot;crashes&quot; |
| ERRORS | &quot;errors&quot; |
| ATTACHMENTS | &quot;attachments&quot; |
| NO_LOGS | &quot;no_logs&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BLOB_STORAGE_CONNECTION_STRING | &quot;blob_storage_connection_string&quot; |
| APPLICATION_INSIGHTS_INSTRUMENTATION_KEY | &quot;application_insights_instrumentation_key&quot; |
| BLOB_STORAGE_LINKED_SUBSCRIPTION | &quot;blob_storage_linked_subscription&quot; |
| APPLICATION_INSIGHTS_LINKED_SUBSCRIPTION | &quot;application_insights_linked_subscription&quot; |



