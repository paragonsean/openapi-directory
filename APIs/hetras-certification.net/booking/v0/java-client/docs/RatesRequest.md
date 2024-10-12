

# RatesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adults** | **byte[]** | Number of adults per room. |  |
|**arrivalDate** | **OffsetDateTime** | Date of arrival for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. |  |
|**channelCode** | **String** | Channel Code the rate plan needs to be configured for. |  |
|**departureDate** | **OffsetDateTime** | Date of departure for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. |  |
|**expand** | [**ExpandEnum**](#ExpandEnum) | Expand the rates breakdown if required. |  [optional] |
|**groupCode** | **String** | Only return offers for the specified group code. |  [optional] |
|**hotelId** | **Integer** | Specifies the hotel id to request offers for. |  |
|**ratePlanCode** | **String** | Only return offers for the specified room type code. |  [optional] |
|**roomType** | **String** | Only return offers with rates for the specified room type code. |  [optional] |
|**rooms** | **byte[]** | Number of rooms (default is 1). |  [optional] |



## Enum: ExpandEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| BREAKDOWN | &quot;Breakdown&quot; |



