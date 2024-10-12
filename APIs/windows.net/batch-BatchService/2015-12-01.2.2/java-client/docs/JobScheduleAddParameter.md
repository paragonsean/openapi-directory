

# JobScheduleAddParameter

A job schedule that allows recurring jobs by specifying when to run jobs and a specification used to create each job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Gets or sets the display name for the schedule. |  [optional] |
|**id** | **String** | Gets or sets a string that uniquely identifies the schedule within the account. A GUID is recommended. |  |
|**jobSpecification** | [**JobSpecification**](JobSpecification.md) |  |  |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | Gets or sets a list of name-value pairs associated with the schedule as metadata. |  [optional] |
|**schedule** | [**Schedule**](Schedule.md) |  |  |



