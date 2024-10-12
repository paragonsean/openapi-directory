

# Key

Key of a result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advanceBookingWindow** | **Integer** | The number of days in advance the user wants to book the itinerary. If &#x60;advanceBookingWindow&#x60; is not a value of the &#x60;aggregateBy&#x60; parameter in the request call, then the &#x60;advanceBookingWindow&#x60; field is not returned in the &#x60;Key&#x60;. |  [optional] |
|**checkinDate** | [**Date**](Date.md) |  |  [optional] |
|**date** | [**Date**](Date.md) |  |  [optional] |
|**deviceType** | [**DeviceTypeEnum**](#DeviceTypeEnum) | The user’s device type. If &#x60;deviceType&#x60; is not a value of the &#x60;aggregateBy&#x60; parameter in the request call, then the &#x60;deviceType&#x60; field is not returned in the &#x60;Key&#x60;. |  [optional] |
|**hotelRegionCode** | **String** | CLDR region code of the country/region of the hotel. If &#x60;hotelRegionCode&#x60; is not a value of the &#x60;aggregateBy&#x60; parameter in the request call, then the &#x60;hotelRegionCode&#x60; field is not returned in the &#x60;Key&#x60;. |  [optional] |
|**lengthOfStayDays** | **Integer** | The number of nights for the itinerary. If &#x60;lengthOfStayDays&#x60; is not a value of the &#x60;aggregateBy&#x60; parameter in the request call, then the &#x60;lengthOfStayDays&#x60; field is not returned in the &#x60;Key&#x60;. |  [optional] |
|**occupancy** | **Integer** | The total occupancy of the itinerary. If &#x60;occupancy&#x60; is not a value of the &#x60;aggregateBy&#x60; parameter in the request call, then the &#x60;occupancy&#x60; field is not returned in the &#x60;Key&#x60;. |  [optional] |
|**partnerHotelId** | **String** | Partner&#39;s hotel ID. If &#x60;partnerHotelId&#x60; is not a value of the &#x60;aggregateBy&#x60; parameter in the request call, then the &#x60;partnerHotelId&#x60; field is not returned in the &#x60;Key&#x60;. |  [optional] |
|**userRegionCode** | **String** | ISO 3116 region code of the country/region of the user. If &#x60;userRegionCode&#x60; is not a value of the &#x60;aggregateBy&#x60; parameter in the request call, then the &#x60;userRegionCode&#x60; field is not returned in the &#x60;Key&#x60;. |  [optional] |



## Enum: DeviceTypeEnum

| Name | Value |
|---- | -----|
| DEVICE_UNSPECIFIED | &quot;DEVICE_UNSPECIFIED&quot; |
| DEVICE_UNKNOWN | &quot;DEVICE_UNKNOWN&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| MOBILE | &quot;MOBILE&quot; |
| TABLET | &quot;TABLET&quot; |



