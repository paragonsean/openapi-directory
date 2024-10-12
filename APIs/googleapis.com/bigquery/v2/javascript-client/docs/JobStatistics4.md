# BigQueryApi.JobStatistics4

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationUriFileCounts** | **[String]** | Output only. Number of files per destination URI or URI pattern specified in the extract configuration. These values will be in the same order as the URIs specified in the &#39;destinationUris&#39; field. | [optional] [readonly] 
**inputBytes** | **String** | Output only. Number of user bytes extracted into the result. This is the byte count as computed by BigQuery for billing purposes and doesn&#39;t have any relationship with the number of actual result bytes extracted in the desired format. | [optional] [readonly] 
**timeline** | [**[QueryTimelineSample]**](QueryTimelineSample.md) | Output only. Describes a timeline of job execution. | [optional] [readonly] 


