# BigQueryApi.JobConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy** | [**JobConfigurationTableCopy**](JobConfigurationTableCopy.md) |  | [optional] 
**dryRun** | **Boolean** | Optional. If set, don&#39;t actually run this job. A valid query will return a mostly empty response with some processing statistics, while an invalid query will return the same error it would if it wasn&#39;t a dry run. Behavior of non-query jobs is undefined. | [optional] 
**extract** | [**JobConfigurationExtract**](JobConfigurationExtract.md) |  | [optional] 
**jobTimeoutMs** | **String** | Optional. Job timeout in milliseconds. If this time limit is exceeded, BigQuery might attempt to stop the job. | [optional] 
**jobType** | **String** | Output only. The type of the job. Can be QUERY, LOAD, EXTRACT, COPY or UNKNOWN. | [optional] 
**labels** | **{String: String}** | The labels associated with this job. You can use these to organize and group your jobs. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key. | [optional] 
**load** | [**JobConfigurationLoad**](JobConfigurationLoad.md) |  | [optional] 
**query** | [**JobConfigurationQuery**](JobConfigurationQuery.md) |  | [optional] 


