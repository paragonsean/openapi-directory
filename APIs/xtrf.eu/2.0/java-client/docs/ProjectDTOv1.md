

# ProjectDTOv1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoriesIds** | **Set&lt;Long&gt;** |  |  [optional] |
|**contactPersonId** | **Long** |  |  [optional] |
|**contacts** | [**ContactsDTO**](ContactsDTO.md) |  |  [optional] |
|**customFields** |  |  |  [optional] |
|**customerId** | **Long** |  |  [optional] |
|**dates** | [**ProjectDatesDTO**](ProjectDatesDTO.md) |  |  [optional] |
|**finance** | [**FinanceDTO**](FinanceDTO.md) |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**idNumber** | **String** |  |  [optional] |
|**instructions** | [**InstructionsDTO**](InstructionsDTO.md) |  |  [optional] |
|**isClassicProject** | **Boolean** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**projectId** | **String** |  |  [optional] |
|**projectManagerId** | **Long** |  |  [optional] |
|**specializationId** | **Long** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tasks** | [**List&lt;TaskDTO&gt;**](TaskDTO.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| REQUESTED_PROJECT | &quot;REQUESTED_PROJECT&quot; |
| OPENED | &quot;OPENED&quot; |
| CLOSED | &quot;CLOSED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| CLAIM | &quot;CLAIM&quot; |



