

# PriceCoverageBucket

Coverage stats for one combination of advance booking window and length of stay.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advanceBookingWindowRange** | [**AdvanceBookingWindowRangeEnum**](#AdvanceBookingWindowRangeEnum) | Advance booking window range. |  [optional] |
|**availablePriceCount** | **String** | Number of prices for this advance booking window bucket and length of stay bucket. |  [optional] |
|**lengthOfStayRange** | [**LengthOfStayRangeEnum**](#LengthOfStayRangeEnum) | Length of stay range. |  [optional] |
|**priceCoveragePercent** | **Double** | The percent of itineraries for which you have coverage for this advance booking window bucket and length of stay bucket. |  [optional] |



## Enum: AdvanceBookingWindowRangeEnum

| Name | Value |
|---- | -----|
| ADVANCE_BOOKING_WINDOW_RANGE_UNSPECIFIED | &quot;ADVANCE_BOOKING_WINDOW_RANGE_UNSPECIFIED&quot; |
| ADVANCE_BOOKING_WINDOW_RANGE_UNKNOWN | &quot;ADVANCE_BOOKING_WINDOW_RANGE_UNKNOWN&quot; |
| DAYS_0_TO_30 | &quot;DAYS_0_TO_30&quot; |
| DAYS_31_TO_60 | &quot;DAYS_31_TO_60&quot; |
| DAYS_61_TO_90 | &quot;DAYS_61_TO_90&quot; |
| DAYS_91_TO_120 | &quot;DAYS_91_TO_120&quot; |
| DAYS_121_TO_150 | &quot;DAYS_121_TO_150&quot; |
| DAYS_151_TO_180 | &quot;DAYS_151_TO_180&quot; |
| DAYS_181_TO_210 | &quot;DAYS_181_TO_210&quot; |
| DAYS_211_TO_240 | &quot;DAYS_211_TO_240&quot; |
| DAYS_241_TO_270 | &quot;DAYS_241_TO_270&quot; |
| DAYS_271_TO_300 | &quot;DAYS_271_TO_300&quot; |
| DAYS_301_TO_330 | &quot;DAYS_301_TO_330&quot; |



## Enum: LengthOfStayRangeEnum

| Name | Value |
|---- | -----|
| RANGE_UNSPECIFIED | &quot;LENGTH_OF_STAY_RANGE_UNSPECIFIED&quot; |
| RANGE_UNKNOWN | &quot;LENGTH_OF_STAY_RANGE_UNKNOWN&quot; |
| _1_TO_7 | &quot;LENGTH_OF_STAY_1_TO_7&quot; |
| _8_TO_14 | &quot;LENGTH_OF_STAY_8_TO_14&quot; |
| _15_TO_30 | &quot;LENGTH_OF_STAY_15_TO_30&quot; |



