

# GetAddonsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adults** | **byte[]** | Number of adults per room. |  |
|**arrivalDate** | **OffsetDateTime** | Date from when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. |  |
|**channelCode** | **String** | Channel Code the rate plan needs to be configured for. |  |
|**departureDate** | **OffsetDateTime** | Date until when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;.              This is usually the departure date of the reservation. |  |
|**expand** | [**ExpandEnum**](#ExpandEnum) | Expand the rates breakdown if required. |  [optional] |
|**hotelId** | **Integer** | Specifies the hotel id to request offers for. |  |
|**ratePlanCode** | **String** | Only return offers for the specified rate plan code. |  |
|**roomType** | **String** | Only return offers for the specified room type code. |  |
|**rooms** | **byte[]** | Number of rooms. |  |



## Enum: ExpandEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| BREAKDOWN | &quot;Breakdown&quot; |



