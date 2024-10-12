# RubrikRestApi.JobMonitoringInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataToTransfer** | **Number** | Amount of data to transfer in bytes. | [optional] 
**dataTransferred** | **Number** | The amount of data transferred as part of the job in bytes. | [optional] 
**duration** | **Number** | The number of seconds since the job started to active jobs. The number of seconds the job ran for completed jobs. | [optional] 
**endTime** | **Date** | End time of the job. Leave this value empty for queued and running jobs. | [optional] 
**errorInfo** | **String** | Description of error information for the job. | [optional] 
**eventSeriesId** | **String** | The event series id associated with the job. | 
**isFirstFullSnapshot** | **Boolean** | A Boolean value that determines whether or not the job associated with the event is a first full snapshot backup. | [optional] 
**isLogTask** | **Boolean** | A boolean value indication if the job is a log related job. | 
**isOnDemand** | **Boolean** | A boolean value indication if the job is a an on demand job. | 
**jobMonitoringState** | [**JobMonitoringState**](JobMonitoringState.md) |  | 
**jobStatus** | [**JobMonitoringStatus**](JobMonitoringStatus.md) |  | 
**jobType** | [**JobMonitoringTaskType**](JobMonitoringTaskType.md) |  | 
**lastSuccessfulJobTime** | **Date** | Time of the last successful job of the same job type. The return value is None if no successful jobs are present. | [optional] 
**lastUpdatedTime** | **Date** | The time the status for the job has been updated. | 
**locationId** | **String** | Id of the location of the object. | [optional] 
**locationName** | **String** | Location Name. | [optional] 
**maximumAttemptsForJob** | **Number** | The maximum number of times the job will run in case of a failure. | [optional] 
**nextJobTime** | **Date** | Expected start time of the next job of the same job type. The return value is None if no new job is scheduled. | [optional] 
**nodeId** | **String** | Id of the node the job is running on. | [optional] 
**objectId** | **String** | The managed id of the object. | 
**objectLogicalSize** | **Number** | The object size in bytes. | [optional] 
**objectName** | **String** | The name of the object in the job. | [optional] 
**objectType** | [**ReportableObjectType**](ReportableObjectType.md) |  | [optional] 
**retryCount** | **Number** | The number of times the job has retired. | [optional] 
**retryStatus** | [**JobMonitoringRetryStatus**](JobMonitoringRetryStatus.md) |  | 
**slaDomainId** | **String** | Sla Domain Id. | [optional] 
**slaDomainName** | **String** | Sla Domain name. | [optional] 
**sourceClusterName** | **String** | For replication jobs, this stores the source cluster name. Leave this value empty for other jobs. | [optional] 
**startTime** | **Date** | Start time for running or completed jobs. It is the scheduled start time for Queued jobs. | 
**throughput** | **Number** | The throughput for running or completed jobs (measured in bytes/s). When no running or completed jobs exist no value is provided. | [optional] 
**warningCount** | **Number** | The number of warning events in the event series associated with the job. | [optional] 


