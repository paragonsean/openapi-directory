# CloudDataprocApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **Boolean** | Output only. Indicates whether the job is completed. If the value is false, the job is still in progress. If true, the job is completed, and status.state field will indicate if it was successful, failed, or cancelled. | [optional] [readonly] 
**driverControlFilesUri** | **String** | Output only. If present, the location of miscellaneous control files which can be used as part of job setup and handling. If not present, control files might be placed in the same location as driver_output_uri. | [optional] [readonly] 
**driverOutputResourceUri** | **String** | Output only. A URI pointing to the location of the stdout of the job&#39;s driver program. | [optional] [readonly] 
**driverSchedulingConfig** | [**DriverSchedulingConfig**](DriverSchedulingConfig.md) |  | [optional] 
**flinkJob** | [**FlinkJob**](FlinkJob.md) |  | [optional] 
**hadoopJob** | [**HadoopJob**](HadoopJob.md) |  | [optional] 
**hiveJob** | [**HiveJob**](HiveJob.md) |  | [optional] 
**jobUuid** | **String** | Output only. A UUID that uniquely identifies a job within the project over time. This is in contrast to a user-settable reference.job_id that might be reused over time. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. The labels to associate with this job. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a job. | [optional] 
**pigJob** | [**PigJob**](PigJob.md) |  | [optional] 
**placement** | [**JobPlacement**](JobPlacement.md) |  | [optional] 
**prestoJob** | [**PrestoJob**](PrestoJob.md) |  | [optional] 
**pysparkJob** | [**PySparkJob**](PySparkJob.md) |  | [optional] 
**reference** | [**JobReference**](JobReference.md) |  | [optional] 
**scheduling** | [**JobScheduling**](JobScheduling.md) |  | [optional] 
**sparkJob** | [**SparkJob**](SparkJob.md) |  | [optional] 
**sparkRJob** | [**SparkRJob**](SparkRJob.md) |  | [optional] 
**sparkSqlJob** | [**SparkSqlJob**](SparkSqlJob.md) |  | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**statusHistory** | [**[JobStatus]**](JobStatus.md) | Output only. The previous job status. | [optional] [readonly] 
**trinoJob** | [**TrinoJob**](TrinoJob.md) |  | [optional] 
**yarnApplications** | [**[YarnApplication]**](YarnApplication.md) | Output only. The collection of YARN applications spun up by this job.Beta Feature: This report is available for testing purposes only. It might be changed before final release. | [optional] [readonly] 


