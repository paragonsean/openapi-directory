

# ListJobsOutput

Output structure for the ListJobs operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobs** | [**List&lt;Job&gt;**](Job.md) | A list container for Jobs returned by the ListJobs operation. |  [optional] |
|**isTruncated** | **Boolean** | Indicates whether the list of jobs was truncated. If true, then call ListJobs again using the last JobId element as the marker. |  [optional] |



