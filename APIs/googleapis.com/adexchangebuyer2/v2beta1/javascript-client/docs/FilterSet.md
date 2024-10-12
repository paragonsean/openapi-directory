# AdExchangeBuyerApiIi.FilterSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absoluteDateRange** | [**AbsoluteDateRange**](AbsoluteDateRange.md) |  | [optional] 
**breakdownDimensions** | **[String]** | The set of dimensions along which to break down the response; may be empty. If multiple dimensions are requested, the breakdown is along the Cartesian product of the requested dimensions. | [optional] 
**creativeId** | **String** | The ID of the creative on which to filter; optional. This field may be set only for a filter set that accesses account-level troubleshooting data, for example, one whose name matches the &#x60;bidders/_*_/accounts/_*_/filterSets/_*&#x60; pattern. | [optional] 
**dealId** | **String** | The ID of the deal on which to filter; optional. This field may be set only for a filter set that accesses account-level troubleshooting data, for example, one whose name matches the &#x60;bidders/_*_/accounts/_*_/filterSets/_*&#x60; pattern. | [optional] 
**environment** | **String** | The environment on which to filter; optional. | [optional] 
**format** | **String** | Creative format bidded on or allowed to bid on, can be empty. | [optional] 
**formats** | **[String]** | Creative formats bidded on or allowed to bid on, can be empty. Although this field is a list, it can only be populated with a single item. A HTTP 400 bad request error will be returned in the response if you specify multiple items. | [optional] 
**name** | **String** | A user-defined name of the filter set. Filter set names must be unique globally and match one of the patterns: - &#x60;bidders/_*_/filterSets/_*&#x60; (for accessing bidder-level troubleshooting data) - &#x60;bidders/_*_/accounts/_*_/filterSets/_*&#x60; (for accessing account-level troubleshooting data) This field is required in create operations. | [optional] 
**platforms** | **[String]** | The list of platforms on which to filter; may be empty. The filters represented by multiple platforms are ORed together (for example, if non-empty, results must match any one of the platforms). | [optional] 
**publisherIdentifiers** | **[String]** | For Open Bidding partners only. The list of publisher identifiers on which to filter; may be empty. The filters represented by multiple publisher identifiers are ORed together. | [optional] 
**realtimeTimeRange** | [**RealtimeTimeRange**](RealtimeTimeRange.md) |  | [optional] 
**relativeDateRange** | [**RelativeDateRange**](RelativeDateRange.md) |  | [optional] 
**sellerNetworkIds** | **[Number]** | For Authorized Buyers only. The list of IDs of the seller (publisher) networks on which to filter; may be empty. The filters represented by multiple seller network IDs are ORed together (for example, if non-empty, results must match any one of the publisher networks). See [seller-network-ids](https://developers.google.com/authorized-buyers/rtb/downloads/seller-network-ids) file for the set of existing seller network IDs. | [optional] 
**timeSeriesGranularity** | **String** | The granularity of time intervals if a time series breakdown is preferred; optional. | [optional] 



## Enum: [BreakdownDimensionsEnum]


* `BREAKDOWN_DIMENSION_UNSPECIFIED` (value: `"BREAKDOWN_DIMENSION_UNSPECIFIED"`)

* `PUBLISHER_IDENTIFIER` (value: `"PUBLISHER_IDENTIFIER"`)





## Enum: EnvironmentEnum


* `ENVIRONMENT_UNSPECIFIED` (value: `"ENVIRONMENT_UNSPECIFIED"`)

* `WEB` (value: `"WEB"`)

* `APP` (value: `"APP"`)





## Enum: FormatEnum


* `FORMAT_UNSPECIFIED` (value: `"FORMAT_UNSPECIFIED"`)

* `NATIVE_DISPLAY` (value: `"NATIVE_DISPLAY"`)

* `NATIVE_VIDEO` (value: `"NATIVE_VIDEO"`)

* `NON_NATIVE_DISPLAY` (value: `"NON_NATIVE_DISPLAY"`)

* `NON_NATIVE_VIDEO` (value: `"NON_NATIVE_VIDEO"`)





## Enum: [FormatsEnum]


* `FORMAT_UNSPECIFIED` (value: `"FORMAT_UNSPECIFIED"`)

* `NATIVE_DISPLAY` (value: `"NATIVE_DISPLAY"`)

* `NATIVE_VIDEO` (value: `"NATIVE_VIDEO"`)

* `NON_NATIVE_DISPLAY` (value: `"NON_NATIVE_DISPLAY"`)

* `NON_NATIVE_VIDEO` (value: `"NON_NATIVE_VIDEO"`)





## Enum: [PlatformsEnum]


* `PLATFORM_UNSPECIFIED` (value: `"PLATFORM_UNSPECIFIED"`)

* `DESKTOP` (value: `"DESKTOP"`)

* `TABLET` (value: `"TABLET"`)

* `MOBILE` (value: `"MOBILE"`)





## Enum: TimeSeriesGranularityEnum


* `TIME_SERIES_GRANULARITY_UNSPECIFIED` (value: `"TIME_SERIES_GRANULARITY_UNSPECIFIED"`)

* `HOURLY` (value: `"HOURLY"`)

* `DAILY` (value: `"DAILY"`)




