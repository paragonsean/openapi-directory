# AzureIoTCentral.ContinuousDataExport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Display name of the continuous data export. | [optional] 
**enabled** | **Boolean** | Boolean indicating whether the continuous data export should be running or not. | 
**endpoint** | [**Endpoint**](Endpoint.md) |  | 
**etag** | **String** | ETag used to prevent conflict in continuous data export updates. | [optional] 
**id** | **String** | Unique ID of the continuous data export. | [optional] [readonly] 
**sources** | **[String]** | Data sources to export to the endpoint. | 
**status** | **String** | Indicates whether the continuous data export is starting, running, etc. | [optional] [readonly] 



## Enum: [SourcesEnum]


* `devices` (value: `"devices"`)

* `deviceTemplates` (value: `"deviceTemplates"`)

* `telemetry` (value: `"telemetry"`)




