

# JobReference

A job reference is a fully qualified identifier for referring to a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | **String** | Required. The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters. |  [optional] |
|**location** | **String** | Optional. The geographic location of the job. The default value is US. For more information about BigQuery locations, see: https://cloud.google.com/bigquery/docs/locations |  [optional] |
|**projectId** | **String** | Required. The ID of the project containing this job. |  [optional] |



