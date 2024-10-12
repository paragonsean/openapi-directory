# AppCenterClient.ExportConfigurationsList200ResponseValuesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **String** | Creation time in ISO 8601 format | 
**exportConfiguration** | [**ExportConfigurationsList200ResponseValuesInnerExportConfiguration**](ExportConfigurationsList200ResponseValuesInnerExportConfiguration.md) |  | [optional] 
**exportEntities** | **[String]** |  | [optional] 
**exportType** | **String** | Target resource type of export configuration | 
**id** | **String** | Export configuration id | 
**lastRunTime** | **String** | Latest time in ISO 8601 format when export completed successfully | [optional] 
**resourceGroup** | **String** | resource group for the storage account/App Insights resource | [optional] 
**resourceName** | **String** | Storage accout or Appinsights resource name | [optional] 
**state** | **String** | State of the export job | 
**stateInfo** | **String** | Additional information about export configuration state | [optional] 



## Enum: [ExportEntitiesEnum]


* `crashes` (value: `"crashes"`)

* `errors` (value: `"errors"`)

* `attachments` (value: `"attachments"`)

* `no_logs` (value: `"no_logs"`)





## Enum: ExportTypeEnum


* `BlobStorage` (value: `"BlobStorage"`)

* `AppInsights` (value: `"AppInsights"`)





## Enum: StateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)

* `Pending` (value: `"Pending"`)

* `Deleted` (value: `"Deleted"`)

* `Invalid` (value: `"Invalid"`)




