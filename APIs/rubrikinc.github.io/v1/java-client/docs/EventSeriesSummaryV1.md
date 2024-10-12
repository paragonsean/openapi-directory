

# EventSeriesSummaryV1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveTargetName** | **String** | The name of the archive target related to the archival task. |  [optional] |
|**dataToTransfer** | **Long** | The amount of data the job corresponding to the event needs to transfer. |  [optional] |
|**dataTransferred** | **Long** | The total amount of data that has been transferred by the event or job to date. |  [optional] |
|**duration** | **String** | The current run time of the job that corresponds to the event series. For completed jobs, this time is equal to the total run time of the job (endTime - startTime). For an in-progress job, this time is equal to the Current Time minus the startTime. This field is empty for event series that do not correspond to a job. |  [optional] |
|**endTime** | **OffsetDateTime** | For event series that correspond to a job, the time when the job finished. For a completed event series, the time of the last event in the series. This field is empty for jobs that have not completed or for event series that do not correspond to a job. |  [optional] |
|**estimatedTimeRemaining** | **String** | The estimated time remaining of the job that corresponds to the event series. This field is empty for event series that do not correspond to a job. |  [optional] |
|**eventDetailList** | [**List&lt;EventSummaryV1&gt;**](EventSummaryV1.md) | List of the events in the event series. |  |
|**eventSeriesId** | **String** | The ID of event series. |  |
|**eventSeriesStatus** | **EventSeriesStatusV1** |  |  [optional] |
|**hasJob** | **Boolean** | A Boolean value that specifies whether the event series is linked to a job on the backend. When this value is &#39;true,&#39; the event series is linked to a job on the backend. When this value is &#39;false,&#39; the event series is not linked to a job on the backend. |  |
|**isFirstFullSnapshot** | **Boolean** | A Boolean value that determines whether the job associated with the event is a first full snapshot backup. |  [optional] |
|**isOnDemand** | **Boolean** | Boolean value of true indicates an on demand job. |  [optional] |
|**isSlaRetentionLocked** | **Boolean** | Boolean that indicates whether an SLA Domain is Retention Locked. When the value is true the SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**location** | **String** | The host of the object associated with the latest event. |  [optional] |
|**logicalSize** | **Long** | The logical size of the object related to the event series. |  [optional] |
|**nodeIds** | **String** | The IDs of the nodes where the job associated with the event is running. |  [optional] |
|**numberOfRetries** | **Long** | The number of times the job has been retried. |  [optional] |
|**objectId** | **String** | The ID of the object associated with the latest event. |  [optional] |
|**objectName** | **String** | The name of the object associated with the latest event. |  [optional] |
|**objectType** | **ObjectTypeV1** |  |  [optional] |
|**progressPercentage** | **String** | The progress percentage of the event series. |  [optional] |
|**remoteClusterName** | **String** | The name of the remote cluster related to the replication task. |  [optional] |
|**slaId** | **String** | The ID of the SLA Domain associated with this job. |  [optional] |
|**slaName** | **String** | The name of the SLA Domain associated with the job, if any. This field is empty for jobs that are not driven by a SLA Domain. |  [optional] |
|**startTime** | **OffsetDateTime** | The time when the job started. Only applicable to the event series that correspond to a job. |  [optional] |
|**status** | **EventStatusV1** |  |  |
|**taskType** | **String** | Type of the event series. Matches the event type.  |  |
|**throughput** | **Long** | The average rate of data transfer, measured in bytes per second. This rate is the total amount of data transferred divided by the total time required by the transfer. |  [optional] |
|**username** | **String** | The username of the user-initiated job. This field is empty for jobs that are not user-initiated. |  [optional] |



