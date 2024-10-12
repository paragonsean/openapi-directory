

# JobStatistics3

Statistics for a load job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**badRecords** | **String** | Output only. The number of bad records encountered. Note that if the job has failed because of more bad records encountered than the maximum allowed in the load job configuration, then this number can be less than the total number of bad records present in the input data. |  [optional] [readonly] |
|**inputFileBytes** | **String** | Output only. Number of bytes of source data in a load job. |  [optional] [readonly] |
|**inputFiles** | **String** | Output only. Number of source files in a load job. |  [optional] [readonly] |
|**outputBytes** | **String** | Output only. Size of the loaded data in bytes. Note that while a load job is in the running state, this value may change. |  [optional] [readonly] |
|**outputRows** | **String** | Output only. Number of rows imported in a load job. Note that while an import job is in the running state, this value may change. |  [optional] [readonly] |
|**timeline** | [**List&lt;QueryTimelineSample&gt;**](QueryTimelineSample.md) | Output only. Describes a timeline of job execution. |  [optional] [readonly] |



