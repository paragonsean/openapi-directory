

# TaskTemplate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** |  |  [optional] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**defaultAssigneeGroup** | **Integer** |  |  [optional] |
|**defaultAssigneeUser** | **String** |  |  [optional] |
|**defaultCategory** | **Integer** |  |  [optional] |
|**defaultDueDateOffset** | **String** | Offset due date, format should follow &#x60;\&quot;[DD] [HH:[MM:]]ss[.uuuuuu]\&quot;&#x60; |  [optional] |
|**defaultNote** | **String** |  |  [optional] |
|**defaultPriority** | [**DefaultPriorityEnum**](#DefaultPriorityEnum) | Can be one of the following 10(Low), 20(Medium), 30(High), 40(Urgent) |  [optional] |
|**defaultStatus** | **Integer** |  |  [optional] |
|**defaultTitle** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**practiceGroup** | **String** |  |  [optional] [readonly] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: DefaultPriorityEnum

| Name | Value |
|---- | -----|
| _10 | &quot;10&quot; |
| _20 | &quot;20&quot; |
| _30 | &quot;30&quot; |
| _40 | &quot;40&quot; |



