

# JobMonitoringInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataToTransfer** | **Long** | Amount of data to transfer in bytes. |  [optional] |
|**dataTransferred** | **Long** | The amount of data transferred as part of the job in bytes. |  [optional] |
|**duration** | **Long** | The number of seconds since the job started to active jobs. The number of seconds the job ran for completed jobs. |  [optional] |
|**endTime** | **OffsetDateTime** | End time of the job. Leave this value empty for queued and running jobs. |  [optional] |
|**errorInfo** | **String** | Description of error information for the job. |  [optional] |
|**eventSeriesId** | **String** | The event series id associated with the job. |  |
|**isFirstFullSnapshot** | **Boolean** | A Boolean value that determines whether or not the job associated with the event is a first full snapshot backup. |  [optional] |
|**isLogTask** | **Boolean** | A boolean value indication if the job is a log related job. |  |
|**isOnDemand** | **Boolean** | A boolean value indication if the job is a an on demand job. |  |
|**jobMonitoringState** | **JobMonitoringState** |  |  |
|**jobStatus** | **JobMonitoringStatus** |  |  |
|**jobType** | **JobMonitoringTaskType** |  |  |
|**lastSuccessfulJobTime** | **OffsetDateTime** | Time of the last successful job of the same job type. The return value is None if no successful jobs are present. |  [optional] |
|**lastUpdatedTime** | **OffsetDateTime** | The time the status for the job has been updated. |  |
|**locationId** | **String** | Id of the location of the object. |  [optional] |
|**locationName** | **String** | Location Name. |  [optional] |
|**maximumAttemptsForJob** | **Integer** | The maximum number of times the job will run in case of a failure. |  [optional] |
|**nextJobTime** | **OffsetDateTime** | Expected start time of the next job of the same job type. The return value is None if no new job is scheduled. |  [optional] |
|**nodeId** | **String** | Id of the node the job is running on. |  [optional] |
|**objectId** | **String** | The managed id of the object. |  |
|**objectLogicalSize** | **Long** | The object size in bytes. |  [optional] |
|**objectName** | **String** | The name of the object in the job. |  [optional] |
|**objectType** | **ReportableObjectType** |  |  [optional] |
|**retryCount** | **Integer** | The number of times the job has retired. |  [optional] |
|**retryStatus** | **JobMonitoringRetryStatus** |  |  |
|**slaDomainId** | **String** | Sla Domain Id. |  [optional] |
|**slaDomainName** | **String** | Sla Domain name. |  [optional] |
|**sourceClusterName** | **String** | For replication jobs, this stores the source cluster name. Leave this value empty for other jobs. |  [optional] |
|**startTime** | **OffsetDateTime** | Start time for running or completed jobs. It is the scheduled start time for Queued jobs. |  |
|**throughput** | **Long** | The throughput for running or completed jobs (measured in bytes/s). When no running or completed jobs exist no value is provided. |  [optional] |
|**warningCount** | **Integer** | The number of warning events in the event series associated with the job. |  [optional] |



