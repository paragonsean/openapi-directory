

# PriceAccuracyRow

A price accuracy row.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adultOccupancy** | **Integer** | The number of adults in the occupancy details of the validation query. |  [optional] |
|**affectsScore** | **Boolean** | True if this row affects the placement of a price. This field has been renamed to “Affects placement” in Hotel Center. |  [optional] |
|**cachedPriceRecord** | [**PriceRecord**](PriceRecord.md) |  |  [optional] |
|**checkinDate** | [**Date**](Date.md) |  |  [optional] |
|**childOccupancy** | **Integer** | The number of children in the occupancy details of the validation query. |  [optional] |
|**correctionTime** | **String** | Time at which an incorrect price is updated to a correct price. |  [optional] |
|**deviceType** | [**DeviceTypeEnum**](#DeviceTypeEnum) | The user&#39;s device type. |  [optional] |
|**fetchedPriceRecord** | [**PriceRecord**](PriceRecord.md) |  |  [optional] |
|**finalDomain** | **String** | The domain of the final page from which prices are read. |  [optional] |
|**hotel** | **String** | Partner-defined hotel ID. |  [optional] |
|**hotelCountryCode** | **String** | The country of the hotel (based on address). |  [optional] |
|**lengthOfStayDays** | **Integer** | Length of stay. |  [optional] |
|**mismatchReason** | [**MismatchReasonEnum**](#MismatchReasonEnum) | The reason why the fetched price didn&#39;t match the cached price. |  [optional] |
|**rateRuleId** | **String** | The rate rule of the advertised price for non-public rates. |  [optional] |
|**signalSource** | [**SignalSourceEnum**](#SignalSourceEnum) | Source of the price accuracy signal. |  [optional] |
|**url** | **String** | Initial URL visited on the partner website. |  [optional] |
|**userRegionCode** | **String** | The user&#39;s region. |  [optional] |



## Enum: DeviceTypeEnum

| Name | Value |
|---- | -----|
| DEVICE_UNSPECIFIED | &quot;DEVICE_UNSPECIFIED&quot; |
| DEVICE_UNKNOWN | &quot;DEVICE_UNKNOWN&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| MOBILE | &quot;MOBILE&quot; |
| TABLET | &quot;TABLET&quot; |



## Enum: MismatchReasonEnum

| Name | Value |
|---- | -----|
| MISMATCH_REASON_UNSPECIFIED | &quot;MISMATCH_REASON_UNSPECIFIED&quot; |
| MISMATCH_REASON_UNKNOWN | &quot;MISMATCH_REASON_UNKNOWN&quot; |
| TAX_MISMATCH | &quot;TAX_MISMATCH&quot; |
| ROOM_UNAVAILABLE | &quot;ROOM_UNAVAILABLE&quot; |
| SITE_ERROR | &quot;SITE_ERROR&quot; |
| PRICE_FEED_DELAYED | &quot;PRICE_FEED_DELAYED&quot; |
| DISCOUNT_MISSING | &quot;DISCOUNT_MISSING&quot; |
| INCORRECT_DISCOUNT_VALUE | &quot;INCORRECT_DISCOUNT_VALUE&quot; |
| WRONG_ITINERARY | &quot;WRONG_ITINERARY&quot; |



## Enum: SignalSourceEnum

| Name | Value |
|---- | -----|
| SIGNAL_SOURCE_UNSPECIFIED | &quot;SIGNAL_SOURCE_UNSPECIFIED&quot; |
| SIGNAL_SOURCE_UNKNOWN | &quot;SIGNAL_SOURCE_UNKNOWN&quot; |
| FETCHED | &quot;FETCHED&quot; |
| PIXEL | &quot;PIXEL&quot; |



