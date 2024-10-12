# AppCenterClient.ExportConfigurationsList200ResponseValuesInnerExportConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backfill** | **Boolean** | Field to determine if backfilling should occur. The default value is true. If set to false export starts from date and time of config creation. | [optional] 
**exportEntities** | **[String]** |  | [optional] 
**resourceGroup** | **String** | The resource group name on azure | [optional] 
**resourceName** | **String** | The resource name on azure | [optional] 
**type** | **String** | Type of export configuration | 



## Enum: [ExportEntitiesEnum]


* `crashes` (value: `"crashes"`)

* `errors` (value: `"errors"`)

* `attachments` (value: `"attachments"`)

* `no_logs` (value: `"no_logs"`)





## Enum: TypeEnum


* `blob_storage_connection_string` (value: `"blob_storage_connection_string"`)

* `application_insights_instrumentation_key` (value: `"application_insights_instrumentation_key"`)

* `blob_storage_linked_subscription` (value: `"blob_storage_linked_subscription"`)

* `application_insights_linked_subscription` (value: `"application_insights_linked_subscription"`)




