# BatchApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationPolicy** | [**AllocationPolicy**](AllocationPolicy.md) |  | [optional] 
**createTime** | **String** | Output only. When the Job was created. | [optional] [readonly] 
**labels** | **{String: String}** | Labels for the Job. Labels could be user provided or system generated. For example, \&quot;labels\&quot;: { \&quot;department\&quot;: \&quot;finance\&quot;, \&quot;environment\&quot;: \&quot;test\&quot; } You can assign up to 64 labels. [Google Compute Engine label restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) apply. Label names that start with \&quot;goog-\&quot; or \&quot;google-\&quot; are reserved. | [optional] 
**logsPolicy** | [**LogsPolicy**](LogsPolicy.md) |  | [optional] 
**name** | **String** | Output only. Job name. For example: \&quot;projects/123456/locations/us-central1/jobs/job01\&quot;. | [optional] [readonly] 
**notifications** | [**[JobNotification]**](JobNotification.md) | Notification configurations. | [optional] 
**priority** | **String** | Priority of the Job. The valid value range is [0, 100). Default value is 0. Higher value indicates higher priority. A job with higher priority value is more likely to run earlier if all other requirements are satisfied. | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**taskGroups** | [**[TaskGroup]**](TaskGroup.md) | Required. TaskGroups in the Job. Only one TaskGroup is supported now. | [optional] 
**uid** | **String** | Output only. A system generated unique ID for the Job. | [optional] [readonly] 
**updateTime** | **String** | Output only. The last time the Job was updated. | [optional] [readonly] 


