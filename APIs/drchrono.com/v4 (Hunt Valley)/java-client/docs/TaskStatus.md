

# TaskStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** |  |  [optional] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**practiceGroup** | **Integer** |  |  |
|**statusCategory** | [**StatusCategoryEnum**](#StatusCategoryEnum) | Can be one of the following &#x60;O&#x60;(open), &#x60;P&#x60;(In progress), &#x60;H&#x60;(On hold), &#x60;C&#x60;(Complete), default to &#x60;O&#x60;(Open) |  [optional] |
|**taskCategory** | **Integer** | ID of &#x60;/api/task_categories&#x60; |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: StatusCategoryEnum

| Name | Value |
|---- | -----|
| O | &quot;O&quot; |
| P | &quot;P&quot; |
| H | &quot;H&quot; |
| C | &quot;C&quot; |



