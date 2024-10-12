

# ListJobsResponse

A list of jobs in a project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobs** | [**List&lt;Job&gt;**](Job.md) | Output only. Jobs list. |  [optional] [readonly] |
|**nextPageToken** | **String** | Optional. This token is included in the response if there are more results to fetch. To fetch additional results, provide this value as the page_token in a subsequent ListJobsRequest. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Output only. List of jobs with kms_key-encrypted parameters that could not be decrypted. A response to a jobs.get request may indicate the reason for the decryption failure for a specific job. |  [optional] [readonly] |



