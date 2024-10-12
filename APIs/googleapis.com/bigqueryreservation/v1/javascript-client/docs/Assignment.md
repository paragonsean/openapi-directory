# BigQueryReservationApi.Assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | **String** | The resource which will use the reservation. E.g. &#x60;projects/myproject&#x60;, &#x60;folders/123&#x60;, or &#x60;organizations/456&#x60;. | [optional] 
**jobType** | **String** | Which type of jobs will use the reservation. | [optional] 
**name** | **String** | Output only. Name of the resource. E.g.: &#x60;projects/myproject/locations/US/reservations/team1-prod/assignments/123&#x60;. The assignment_id must only contain lower case alphanumeric characters or dashes and the max length is 64 characters. | [optional] [readonly] 
**state** | **String** | Output only. State of the assignment. | [optional] [readonly] 



## Enum: JobTypeEnum


* `JOB_TYPE_UNSPECIFIED` (value: `"JOB_TYPE_UNSPECIFIED"`)

* `PIPELINE` (value: `"PIPELINE"`)

* `QUERY` (value: `"QUERY"`)

* `ML_EXTERNAL` (value: `"ML_EXTERNAL"`)

* `BACKGROUND` (value: `"BACKGROUND"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)




