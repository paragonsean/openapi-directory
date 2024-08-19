

# Health


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the status of the service. |  [optional] |
|**details** | [**Map&lt;String, Health&gt;**](Health.md) | Details of the health of the service. This contains information about the status of the components on which the service depends. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the service. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| UP | &quot;UP&quot; |
| DOWN | &quot;DOWN&quot; |



