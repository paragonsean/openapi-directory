

# CancelBooking404Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) |  |  [optional] |
|**message** | [**MessageEnum**](#MessageEnum) | The specified booking was not found; or, it was not created with this API key |  [optional] |
|**timestamp** | **String** | Timestamp of the request |  [optional] |
|**trackingId** | **String** | Tracking identifier for this error response (useful when seeking support) |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| NOT_FOUND | &quot;NOT_FOUND&quot; |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| BOOKING_NOT_FOUND | &quot;Booking not found&quot; |



