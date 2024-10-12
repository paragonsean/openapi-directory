

# ChangeStatusApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | Invoice Id |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | New status of the invoice |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;Draft&quot; |
| PAID | &quot;Paid&quot; |
| UNPAID | &quot;Unpaid&quot; |
| OVERDUE | &quot;Overdue&quot; |
| VOID | &quot;Void&quot; |



