# BigQueryApi.JobList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | A hash of this page of results. | [optional] 
**jobs** | [**[JobListJobsInner]**](JobListJobsInner.md) | List of jobs that were requested. | [optional] 
**kind** | **String** | The resource type of the response. | [optional] [default to &#39;bigquery#jobList&#39;]
**nextPageToken** | **String** | A token to request the next page of results. | [optional] 
**unreachable** | **[String]** | A list of skipped locations that were unreachable. For more information about BigQuery locations, see: https://cloud.google.com/bigquery/docs/locations. Example: \&quot;europe-west5\&quot; | [optional] 


