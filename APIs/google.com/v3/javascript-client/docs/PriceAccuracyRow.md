# TravelPartnerApi.PriceAccuracyRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adultOccupancy** | **Number** | The number of adults in the occupancy details of the validation query. | [optional] 
**affectsScore** | **Boolean** | True if this row affects the placement of a price. This field has been renamed to “Affects placement” in Hotel Center. | [optional] 
**cachedPriceRecord** | [**PriceRecord**](PriceRecord.md) |  | [optional] 
**checkinDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**childOccupancy** | **Number** | The number of children in the occupancy details of the validation query. | [optional] 
**correctionTime** | **String** | Time at which an incorrect price is updated to a correct price. | [optional] 
**deviceType** | **String** | The user&#39;s device type. | [optional] 
**fetchedPriceRecord** | [**PriceRecord**](PriceRecord.md) |  | [optional] 
**finalDomain** | **String** | The domain of the final page from which prices are read. | [optional] 
**hotel** | **String** | Partner-defined hotel ID. | [optional] 
**hotelCountryCode** | **String** | The country of the hotel (based on address). | [optional] 
**lengthOfStayDays** | **Number** | Length of stay. | [optional] 
**mismatchReason** | **String** | The reason why the fetched price didn&#39;t match the cached price. | [optional] 
**rateRuleId** | **String** | The rate rule of the advertised price for non-public rates. | [optional] 
**signalSource** | **String** | Source of the price accuracy signal. | [optional] 
**url** | **String** | Initial URL visited on the partner website. | [optional] 
**userRegionCode** | **String** | The user&#39;s region. | [optional] 



## Enum: DeviceTypeEnum


* `DEVICE_UNSPECIFIED` (value: `"DEVICE_UNSPECIFIED"`)

* `DEVICE_UNKNOWN` (value: `"DEVICE_UNKNOWN"`)

* `DESKTOP` (value: `"DESKTOP"`)

* `MOBILE` (value: `"MOBILE"`)

* `TABLET` (value: `"TABLET"`)





## Enum: MismatchReasonEnum


* `MISMATCH_REASON_UNSPECIFIED` (value: `"MISMATCH_REASON_UNSPECIFIED"`)

* `MISMATCH_REASON_UNKNOWN` (value: `"MISMATCH_REASON_UNKNOWN"`)

* `TAX_MISMATCH` (value: `"TAX_MISMATCH"`)

* `ROOM_UNAVAILABLE` (value: `"ROOM_UNAVAILABLE"`)

* `SITE_ERROR` (value: `"SITE_ERROR"`)

* `PRICE_FEED_DELAYED` (value: `"PRICE_FEED_DELAYED"`)

* `DISCOUNT_MISSING` (value: `"DISCOUNT_MISSING"`)

* `INCORRECT_DISCOUNT_VALUE` (value: `"INCORRECT_DISCOUNT_VALUE"`)

* `WRONG_ITINERARY` (value: `"WRONG_ITINERARY"`)





## Enum: SignalSourceEnum


* `SIGNAL_SOURCE_UNSPECIFIED` (value: `"SIGNAL_SOURCE_UNSPECIFIED"`)

* `SIGNAL_SOURCE_UNKNOWN` (value: `"SIGNAL_SOURCE_UNKNOWN"`)

* `FETCHED` (value: `"FETCHED"`)

* `PIXEL` (value: `"PIXEL"`)




