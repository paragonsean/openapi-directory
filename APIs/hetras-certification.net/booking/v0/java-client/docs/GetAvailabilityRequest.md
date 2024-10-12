

# GetAvailabilityRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expand** | [**ExpandEnum**](#ExpandEnum) | You can expand the room types breakdown per business day for the availibility numbers if need be. |  [optional] |
|**from** | **OffsetDateTime** | Defines the first business day you would like to get availability numbers for. |  |
|**hotelId** | **Integer** | Specifies the hotel id to request the availability for. |  |
|**to** | **OffsetDateTime** | Defines the last business day you would like to get availability numbers for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. |  |



## Enum: ExpandEnum

| Name | Value |
|---- | -----|
| ROOM_TYPES | &quot;RoomTypes&quot; |



