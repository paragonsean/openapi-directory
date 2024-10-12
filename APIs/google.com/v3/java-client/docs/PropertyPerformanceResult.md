

# PropertyPerformanceResult

Represents a result from querying for the property performance report for an account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsClickCount** | **String** | The total number of ad clicks that were recorded for this result. |  [optional] |
|**adsClickthroughRate** | **Double** | Equal to &#x60;ads_click_count&#x60; divided by &#x60;ads_impression_count&#x60;. |  [optional] |
|**adsImpressionCount** | **String** | The total number of ad impressions that were recorded for this result. |  [optional] |
|**advanceBookingWindow** | [**AdvanceBookingWindowEnum**](#AdvanceBookingWindowEnum) | Difference in days between query date and check-in date in property&#39;s local timezone. Only present if &#x60;advanceBookingWindow&#x60; is specified in &#x60;aggregateBy&#x60; in the request. |  [optional] |
|**brand** | **String** | Partner-specified brand for the property. Only present if &#x60;brand&#x60; is specified in &#x60;aggregateBy&#x60; in the request. |  [optional] |
|**clickCount** | **String** | The total number of free booking link clicks that were recorded for this result. |  [optional] |
|**clickthroughRate** | **Double** | Equal to &#x60;click_count&#x60; divided by &#x60;impression_count&#x60;. |  [optional] |
|**date** | [**Date**](Date.md) |  |  [optional] |
|**deviceType** | [**DeviceTypeEnum**](#DeviceTypeEnum) | The user’s device type. Only present if &#x60;deviceType&#x60; is specified in &#x60;aggregateBy&#x60; in the request. |  [optional] |
|**highIntentUsers** | **Boolean** | Whether the user’s query indicated a strong interest in booking. Only present if &#x60;highIntentUsers&#x60; is specified in &#x60;aggregateBy&#x60; in the request. |  [optional] |
|**impressionCount** | **String** | The total number of free booking link impressions that were recorded for this result. This value is rounded to preserve user privacy. |  [optional] |
|**lengthOfStay** | [**LengthOfStayEnum**](#LengthOfStayEnum) | Number of nights between check-in and check-out dates specified by user. Only present if &#x60;lengthOfStay&#x60; is specified in &#x60;aggregateBy&#x60; in the request. |  [optional] |
|**occupancy** | [**OccupancyEnum**](#OccupancyEnum) | Requested number of people staying at the property. Only present if &#x60;partnerPropertyId&#x60; is specified in &#x60;aggregateBy&#x60; in the request. |  [optional] |
|**partnerPropertyDisplayName** | **String** | Partner&#39;s property name. Only present if &#x60;partnerPropertyDisplayName&#x60; is specified in &#x60;aggregateBy&#x60; in the request. |  [optional] |
|**partnerPropertyId** | **String** | Partner&#39;s property ID. Only present if &#x60;partnerPropertyId&#x60; is specified in &#x60;aggregateBy&#x60; in the request. |  [optional] |
|**propertyRegionCode** | **String** | ISO 3116 region code of the country/region of the property. Only present if &#x60;propertyRegionCode&#x60; is specified in &#x60;aggregateBy&#x60; in the request |  [optional] |
|**userRegionCode** | **String** | ISO 3116 region code of the country/region of the user. Only present if &#x60;userRegionCode&#x60; is specified in &#x60;aggregateBy&#x60; in the request |  [optional] |
|**vrWebsiteButtonClicks** | **String** | The total number of clicks on the \&quot;Website\&quot; button on Google for vacation rentals. |  [optional] |



## Enum: AdvanceBookingWindowEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ADVANCE_BOOKING_WINDOW_UNSPECIFIED&quot; |
| SAME_DAY | &quot;ADVANCE_BOOKING_WINDOW_SAME_DAY&quot; |
| NEXT_DAY | &quot;ADVANCE_BOOKING_WINDOW_NEXT_DAY&quot; |
| DAYS_2_TO_7 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_2_TO_7&quot; |
| DAYS_8_TO_14 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_8_TO_14&quot; |
| DAYS_15_TO_30 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_15_TO_30&quot; |
| DAYS_31_TO_60 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_31_TO_60&quot; |
| DAYS_61_TO_90 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90&quot; |
| DAYS_91_TO_120 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_91_TO_120&quot; |
| DAYS_121_TO_150 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_121_TO_150&quot; |
| DAYS_151_TO_180 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_151_TO_180&quot; |
| DAYS_OVER_180 | &quot;ADVANCE_BOOKING_WINDOW_DAYS_OVER_180&quot; |



## Enum: DeviceTypeEnum

| Name | Value |
|---- | -----|
| DEVICE_UNSPECIFIED | &quot;DEVICE_UNSPECIFIED&quot; |
| DEVICE_UNKNOWN | &quot;DEVICE_UNKNOWN&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| MOBILE | &quot;MOBILE&quot; |
| TABLET | &quot;TABLET&quot; |



## Enum: LengthOfStayEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LENGTH_OF_STAY_UNSPECIFIED&quot; |
| NIGHTS_1 | &quot;LENGTH_OF_STAY_NIGHTS_1&quot; |
| NIGHTS_2 | &quot;LENGTH_OF_STAY_NIGHTS_2&quot; |
| NIGHTS_3 | &quot;LENGTH_OF_STAY_NIGHTS_3&quot; |
| NIGHTS_4_TO_7 | &quot;LENGTH_OF_STAY_NIGHTS_4_TO_7&quot; |
| NIGHTS_8_TO_14 | &quot;LENGTH_OF_STAY_NIGHTS_8_TO_14&quot; |
| NIGHTS_15_TO_21 | &quot;LENGTH_OF_STAY_NIGHTS_15_TO_21&quot; |
| NIGHTS_22_TO_30 | &quot;LENGTH_OF_STAY_NIGHTS_22_TO_30&quot; |
| NIGHTS_OVER_30 | &quot;LENGTH_OF_STAY_NIGHTS_OVER_30&quot; |



## Enum: OccupancyEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OCCUPANCY_UNSPECIFIED&quot; |
| _1 | &quot;OCCUPANCY_1&quot; |
| _2 | &quot;OCCUPANCY_2&quot; |
| _3 | &quot;OCCUPANCY_3&quot; |
| _4 | &quot;OCCUPANCY_4&quot; |
| OVER_4 | &quot;OCCUPANCY_OVER_4&quot; |



