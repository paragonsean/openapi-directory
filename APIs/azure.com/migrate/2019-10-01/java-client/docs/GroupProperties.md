

# GroupProperties

Properties of group resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**areAssessmentsRunning** | **Boolean** | If the assessments are in running state. |  [optional] [readonly] |
|**assessments** | **List&lt;String&gt;** | List of References to Assessments created on this group. |  [optional] [readonly] |
|**createdTimestamp** | **OffsetDateTime** | Time when this group was created. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**groupStatus** | [**GroupStatusEnum**](#GroupStatusEnum) | Whether the group has been created and is valid. |  [optional] [readonly] |
|**machineCount** | **Integer** | Number of machines part of this group. |  [optional] [readonly] |
|**updatedTimestamp** | **OffsetDateTime** | Time when this group was last updated. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |



## Enum: GroupStatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;Created&quot; |
| UPDATED | &quot;Updated&quot; |
| RUNNING | &quot;Running&quot; |
| COMPLETED | &quot;Completed&quot; |
| INVALID | &quot;Invalid&quot; |



