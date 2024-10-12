

# TaskCounts


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Integer** |  |  |
|**completed** | **Integer** |  |  |
|**failed** | **Integer** |  |  |
|**running** | **Integer** |  |  |
|**succeeded** | **Integer** |  |  |
|**validationStatus** | [**ValidationStatusEnum**](#ValidationStatusEnum) | If the validationStatus is unvalidated, then the Batch service has not been able to check state counts against the task states as reported in the List Tasks API. The validationStatus may be unvalidated if the job contains more than 200,000 tasks. |  |



## Enum: ValidationStatusEnum

| Name | Value |
|---- | -----|
| VALIDATED | &quot;validated&quot; |
| UNVALIDATED | &quot;unvalidated&quot; |



