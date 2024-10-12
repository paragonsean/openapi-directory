

# Assignment

An assignment allows a project to submit jobs of a certain type using slots from the specified reservation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignee** | **String** | The resource which will use the reservation. E.g. &#x60;projects/myproject&#x60;, &#x60;folders/123&#x60;, or &#x60;organizations/456&#x60;. |  [optional] |
|**jobType** | [**JobTypeEnum**](#JobTypeEnum) | Which type of jobs will use the reservation. |  [optional] |
|**name** | **String** | Output only. Name of the resource. E.g.: &#x60;projects/myproject/locations/US/reservations/team1-prod/assignments/123&#x60;. The assignment_id must only contain lower case alphanumeric characters or dashes and the max length is 64 characters. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the assignment. |  [optional] [readonly] |



## Enum: JobTypeEnum

| Name | Value |
|---- | -----|
| JOB_TYPE_UNSPECIFIED | &quot;JOB_TYPE_UNSPECIFIED&quot; |
| PIPELINE | &quot;PIPELINE&quot; |
| QUERY | &quot;QUERY&quot; |
| ML_EXTERNAL | &quot;ML_EXTERNAL&quot; |
| BACKGROUND | &quot;BACKGROUND&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



