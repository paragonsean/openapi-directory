# RubrikRestApi.JobMonitoringCsvDownloadResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downloadLink** | **String** | The download link for the CSV file. | 
**jobEventStatus** | [**JobMonitoringStatus**](JobMonitoringStatus.md) |  | [optional] 
**jobMonitoringState** | [**JobMonitoringState**](JobMonitoringState.md) |  | 
**jobTaskType** | [**JobMonitoringTaskType**](JobMonitoringTaskType.md) |  | [optional] 
**objectName** | **String** | The requested object name (if applicable). | [optional] 
**objectType** | [**ReportableObjectType**](ReportableObjectType.md) |  | [optional] 
**shouldIncludeLogRelatedJob** | **Boolean** | A Boolean that specifies whether log-related jobs are included. When this value is &#39;true,&#39; log-related jobs are included. | 


