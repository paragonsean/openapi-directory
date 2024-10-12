

# EmployeeCompensation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | **Currency** |  |  [optional] |
|**effectiveDate** | **String** | The date on which a change to an employee&#39;s compensation takes effect. |  [optional] |
|**flsaStatus** | [**FlsaStatusEnum**](#FlsaStatusEnum) | The FLSA status for this compensation. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**jobId** | **String** | The ID of the job to which the compensation belongs. |  [optional] [readonly] |
|**paymentFrequency** | **PaymentFrequency** |  |  [optional] |
|**paymentUnit** | **PaymentUnit** |  |  [optional] |
|**rate** | **BigDecimal** | The amount paid per payment unit. |  [optional] |



## Enum: FlsaStatusEnum

| Name | Value |
|---- | -----|
| EXEMPT | &quot;exempt&quot; |
| SALARIED_NONEXEMPT | &quot;salaried-nonexempt&quot; |
| NONEXEMPT | &quot;nonexempt&quot; |
| OWNER | &quot;owner&quot; |
| OTHER | &quot;other&quot; |



