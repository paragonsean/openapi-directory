# TravelPartnerApi.PropertyPerformanceResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adsClickCount** | **String** | The total number of ad clicks that were recorded for this result. | [optional] 
**adsClickthroughRate** | **Number** | Equal to &#x60;ads_click_count&#x60; divided by &#x60;ads_impression_count&#x60;. | [optional] 
**adsImpressionCount** | **String** | The total number of ad impressions that were recorded for this result. | [optional] 
**advanceBookingWindow** | **String** | Difference in days between query date and check-in date in property&#39;s local timezone. Only present if &#x60;advanceBookingWindow&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**brand** | **String** | Partner-specified brand for the property. Only present if &#x60;brand&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**clickCount** | **String** | The total number of free booking link clicks that were recorded for this result. | [optional] 
**clickthroughRate** | **Number** | Equal to &#x60;click_count&#x60; divided by &#x60;impression_count&#x60;. | [optional] 
**date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**deviceType** | **String** | The user’s device type. Only present if &#x60;deviceType&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**highIntentUsers** | **Boolean** | Whether the user’s query indicated a strong interest in booking. Only present if &#x60;highIntentUsers&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**impressionCount** | **String** | The total number of free booking link impressions that were recorded for this result. This value is rounded to preserve user privacy. | [optional] 
**lengthOfStay** | **String** | Number of nights between check-in and check-out dates specified by user. Only present if &#x60;lengthOfStay&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**occupancy** | **String** | Requested number of people staying at the property. Only present if &#x60;partnerPropertyId&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**partnerPropertyDisplayName** | **String** | Partner&#39;s property name. Only present if &#x60;partnerPropertyDisplayName&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**partnerPropertyId** | **String** | Partner&#39;s property ID. Only present if &#x60;partnerPropertyId&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**propertyRegionCode** | **String** | ISO 3116 region code of the country/region of the property. Only present if &#x60;propertyRegionCode&#x60; is specified in &#x60;aggregateBy&#x60; in the request | [optional] 
**userRegionCode** | **String** | ISO 3116 region code of the country/region of the user. Only present if &#x60;userRegionCode&#x60; is specified in &#x60;aggregateBy&#x60; in the request | [optional] 
**vrWebsiteButtonClicks** | **String** | The total number of clicks on the \&quot;Website\&quot; button on Google for vacation rentals. | [optional] 



## Enum: AdvanceBookingWindowEnum


* `UNSPECIFIED` (value: `"ADVANCE_BOOKING_WINDOW_UNSPECIFIED"`)

* `SAME_DAY` (value: `"ADVANCE_BOOKING_WINDOW_SAME_DAY"`)

* `NEXT_DAY` (value: `"ADVANCE_BOOKING_WINDOW_NEXT_DAY"`)

* `DAYS_2_TO_7` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_2_TO_7"`)

* `DAYS_8_TO_14` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_8_TO_14"`)

* `DAYS_15_TO_30` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_15_TO_30"`)

* `DAYS_31_TO_60` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_31_TO_60"`)

* `DAYS_61_TO_90` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90"`)

* `DAYS_91_TO_120` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_91_TO_120"`)

* `DAYS_121_TO_150` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_121_TO_150"`)

* `DAYS_151_TO_180` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_151_TO_180"`)

* `DAYS_OVER_180` (value: `"ADVANCE_BOOKING_WINDOW_DAYS_OVER_180"`)





## Enum: DeviceTypeEnum


* `DEVICE_UNSPECIFIED` (value: `"DEVICE_UNSPECIFIED"`)

* `DEVICE_UNKNOWN` (value: `"DEVICE_UNKNOWN"`)

* `DESKTOP` (value: `"DESKTOP"`)

* `MOBILE` (value: `"MOBILE"`)

* `TABLET` (value: `"TABLET"`)





## Enum: LengthOfStayEnum


* `UNSPECIFIED` (value: `"LENGTH_OF_STAY_UNSPECIFIED"`)

* `NIGHTS_1` (value: `"LENGTH_OF_STAY_NIGHTS_1"`)

* `NIGHTS_2` (value: `"LENGTH_OF_STAY_NIGHTS_2"`)

* `NIGHTS_3` (value: `"LENGTH_OF_STAY_NIGHTS_3"`)

* `NIGHTS_4_TO_7` (value: `"LENGTH_OF_STAY_NIGHTS_4_TO_7"`)

* `NIGHTS_8_TO_14` (value: `"LENGTH_OF_STAY_NIGHTS_8_TO_14"`)

* `NIGHTS_15_TO_21` (value: `"LENGTH_OF_STAY_NIGHTS_15_TO_21"`)

* `NIGHTS_22_TO_30` (value: `"LENGTH_OF_STAY_NIGHTS_22_TO_30"`)

* `NIGHTS_OVER_30` (value: `"LENGTH_OF_STAY_NIGHTS_OVER_30"`)





## Enum: OccupancyEnum


* `UNSPECIFIED` (value: `"OCCUPANCY_UNSPECIFIED"`)

* `1` (value: `"OCCUPANCY_1"`)

* `2` (value: `"OCCUPANCY_2"`)

* `3` (value: `"OCCUPANCY_3"`)

* `4` (value: `"OCCUPANCY_4"`)

* `OVER_4` (value: `"OCCUPANCY_OVER_4"`)




