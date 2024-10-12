

# ListJobsInput

Input structure for the ListJobs operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxJobs** | **Integer** | Sets the maximum number of jobs returned in the response. If there are additional jobs that were not returned because MaxJobs was exceeded, the response contains &amp;lt;IsTruncated&amp;gt;true&amp;lt;/IsTruncated&amp;gt;. To return the additional jobs, see Marker. |  [optional] |
|**marker** | **String** | Specifies the JOBID to start after when listing the jobs created with your account. AWS Import/Export lists your jobs in reverse chronological order. See MaxJobs. |  [optional] |
|**apIVersion** | **String** | Specifies the version of the client tool. |  [optional] |



