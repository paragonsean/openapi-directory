

# JobList

JobList is the response format for a jobs.list call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | A hash of this page of results. |  [optional] |
|**jobs** | [**List&lt;JobListJobsInner&gt;**](JobListJobsInner.md) | List of jobs that were requested. |  [optional] |
|**kind** | **String** | The resource type of the response. |  [optional] |
|**nextPageToken** | **String** | A token to request the next page of results. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of skipped locations that were unreachable. For more information about BigQuery locations, see: https://cloud.google.com/bigquery/docs/locations. Example: \&quot;europe-west5\&quot; |  [optional] |



