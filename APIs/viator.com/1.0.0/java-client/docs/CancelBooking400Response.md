

# CancelBooking400Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) |  |  [optional] |
|**message** | [**MessageEnum**](#MessageEnum) |  |  [optional] |
|**timestamp** | **String** | Timestamp of the request |  [optional] |
|**trackingId** | **String** | Tracking identifier for this error response (useful when seeking support) |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| BAD_REQUEST | &quot;BAD_REQUEST&quot; |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| MISSING_CANCELLATION_REASON | &quot;Missing cancellation reason&quot; |



