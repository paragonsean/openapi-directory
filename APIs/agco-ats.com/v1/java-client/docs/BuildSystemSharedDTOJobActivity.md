

# BuildSystemSharedDTOJobActivity

A DTO for an IJobActivity

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityID** | **Integer** | The ID of the activity to be run as part of the job |  [optional] |
|**jobActivityID** | **Integer** | The ID of this job activity |  [optional] |
|**jobID** | **Integer** | The ID of the job this job activity belongs to |  [optional] |
|**parameterMappings** | [**List&lt;BuildSystemSharedDTOParameterMapping&gt;**](BuildSystemSharedDTOParameterMapping.md) | The mapping of values from a source to be used for the activity parameters |  [optional] [readonly] |
|**runOrder** | **Integer** | The order of this job activity relative to others in the job |  [optional] |



