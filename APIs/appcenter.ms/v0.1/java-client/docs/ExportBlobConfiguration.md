

# ExportBlobConfiguration

Configuration for export to Blob Storage with blob format

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobPathFormatKind** | [**BlobPathFormatKindEnum**](#BlobPathFormatKindEnum) | The path to the blob when enum set to &#39;WithoutAppId&#39; is &#39;year/month/day/hour/minute&#39; and when set to &#39;WithAppId&#39; is &#39;appId/year/month/day/hour/minute&#39; |  [optional] |
|**backfill** | **Boolean** | Field to determine if backfilling should occur. The default value is true. If set to false export starts from date and time of config creation. |  [optional] |
|**exportEntities** | [**List&lt;ExportEntitiesEnum&gt;**](#List&lt;ExportEntitiesEnum&gt;) |  |  [optional] |
|**resourceGroup** | **String** | The resource group name on azure |  [optional] |
|**resourceName** | **String** | The resource name on azure |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of export configuration |  |



## Enum: BlobPathFormatKindEnum

| Name | Value |
|---- | -----|
| WITHOUT_APP_ID | &quot;WithoutAppId&quot; |
| WITH_APP_ID | &quot;WithAppId&quot; |



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



