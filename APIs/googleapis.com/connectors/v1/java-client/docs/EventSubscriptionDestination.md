

# EventSubscriptionDestination

Message for EventSubscription Destination to act on receiving an event

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoint** | [**EndPoint**](EndPoint.md) |  |  [optional] |
|**serviceAccount** | **String** | Service account needed for runtime plane to trigger IP workflow. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | type of the destination |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| ENDPOINT | &quot;ENDPOINT&quot; |



