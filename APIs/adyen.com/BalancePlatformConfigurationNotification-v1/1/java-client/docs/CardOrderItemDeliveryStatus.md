

# CardOrderItemDeliveryStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | An error message. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the PIN delivery. |  [optional] |
|**trackingNumber** | **String** | The tracking number of the PIN delivery. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;created&quot; |
| DELIVERED | &quot;delivered&quot; |
| NOT_APPLICABLE | &quot;notApplicable&quot; |
| PROCESSING | &quot;processing&quot; |
| PRODUCED | &quot;produced&quot; |
| REJECTED | &quot;rejected&quot; |
| SHIPPED | &quot;shipped&quot; |
| UNKNOWN | &quot;unknown&quot; |



