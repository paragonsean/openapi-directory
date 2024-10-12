

# IssueTimeShiftInstruction

The calculation instruction of billing time. This is used in conjunction with the **service period anchor** to calculate the time the invoice is issued. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chronology** | [**ChronologyEnum**](#ChronologyEnum) | The chronology of the billing time relatively to the service period start. |  |
|**duration** | **Integer** | The number of the units. |  |
|**unit** | [**DueTimeShiftInstructionUnit**](DueTimeShiftInstructionUnit.md) |  |  |



## Enum: ChronologyEnum

| Name | Value |
|---- | -----|
| BEFORE | &quot;before&quot; |



