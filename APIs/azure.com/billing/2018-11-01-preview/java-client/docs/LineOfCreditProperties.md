

# LineOfCreditProperties

The properties of the line of credit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creditLimit** | [**Amount**](Amount.md) |  |  [optional] |
|**reason** | **String** | The reason for the line of credit status when not approved. |  [optional] [readonly] |
|**remainingBalance** | [**Amount**](Amount.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The line of credit status. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;Approved&quot; |
| REJECTED | &quot;Rejected&quot; |



