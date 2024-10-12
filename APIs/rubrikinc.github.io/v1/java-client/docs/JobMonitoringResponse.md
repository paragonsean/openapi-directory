

# JobMonitoringResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afterId** | **String** | Cursor of the last table row sent in the response. Used for setting the cursor when getting the next page of the table. |  [optional] |
|**effectiveSlaDomainId** | **String** | The requested SLA domain id (if applicable). |  [optional] |
|**hasMore** | **Boolean** | A Boolean value that specifies whether or not the list has more elements. This value is &#39;true&#39; when the list has more elements. This value is &#39;false&#39; when the list has no more elements. |  |
|**isFirstFull** | **Boolean** | A Boolean to specify if the jobs are first full backups or not. |  [optional] |
|**jobEventStatus** | **List&lt;JobMonitoringStatus&gt;** | The requested event status of the jobs (if applicable). |  [optional] |
|**jobMonitoringInfoList** | [**List&lt;JobMonitoringInfo&gt;**](JobMonitoringInfo.md) | A list of jobs. |  |
|**jobType** | **JobMonitoringTaskType** |  |  [optional] |
|**lastUpdateTime** | **OffsetDateTime** | The earliest possible time at which the latest update to all rows has been made. |  [optional] |
|**nodeName** | **String** | The requested node (if applicable). |  [optional] |
|**objectName** | **String** | The requested object name (if applicable). |  [optional] |
|**objectType** | **ReportableObjectType** |  |  [optional] |
|**shouldIncludeLogRelatedJob** | **Boolean** | A Boolean to specify whether or not to include log-related jobs. |  |



