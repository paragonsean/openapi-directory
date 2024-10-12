# TravelPartnerApi.FreeBookingLinksResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clickCount** | **String** | The total number of clicks that were recorded for this result. | [optional] 
**date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**deviceType** | **String** | The user’s device type. Only present if &#x60;deviceType&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**partnerHotelDisplayName** | **String** | Partner&#39;s hotel name. Only present if &#x60;partnerHotelDisplayName&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**partnerHotelId** | **String** | Partner&#39;s hotel ID. Only present if &#x60;partnerHotelId&#x60; is specified in &#x60;aggregateBy&#x60; in the request. | [optional] 
**userRegionCode** | **String** | ISO 3116 region code of the country/region of the user. Only present if &#x60;userRegionCode&#x60; is specified in &#x60;aggregateBy&#x60; in the request | [optional] 



## Enum: DeviceTypeEnum


* `DEVICE_UNSPECIFIED` (value: `"DEVICE_UNSPECIFIED"`)

* `DEVICE_UNKNOWN` (value: `"DEVICE_UNKNOWN"`)

* `DESKTOP` (value: `"DESKTOP"`)

* `MOBILE` (value: `"MOBILE"`)

* `TABLET` (value: `"TABLET"`)




