

# FilterSet

A set of filters that is applied to a request for data. Within a filter set, an AND operation is performed across the filters represented by each field. An OR operation is performed across the filters represented by the multiple values of a repeated field, for example, \"format=VIDEO AND deal_id=12 AND (seller_network_id=34 OR seller_network_id=56)\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**absoluteDateRange** | [**AbsoluteDateRange**](AbsoluteDateRange.md) |  |  [optional] |
|**breakdownDimensions** | [**List&lt;BreakdownDimensionsEnum&gt;**](#List&lt;BreakdownDimensionsEnum&gt;) | The set of dimensions along which to break down the response; may be empty. If multiple dimensions are requested, the breakdown is along the Cartesian product of the requested dimensions. |  [optional] |
|**creativeId** | **String** | The ID of the creative on which to filter; optional. This field may be set only for a filter set that accesses account-level troubleshooting data, for example, one whose name matches the &#x60;bidders/_*_/accounts/_*_/filterSets/_*&#x60; pattern. |  [optional] |
|**dealId** | **String** | The ID of the deal on which to filter; optional. This field may be set only for a filter set that accesses account-level troubleshooting data, for example, one whose name matches the &#x60;bidders/_*_/accounts/_*_/filterSets/_*&#x60; pattern. |  [optional] |
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | The environment on which to filter; optional. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Creative format bidded on or allowed to bid on, can be empty. |  [optional] |
|**formats** | [**List&lt;FormatsEnum&gt;**](#List&lt;FormatsEnum&gt;) | Creative formats bidded on or allowed to bid on, can be empty. Although this field is a list, it can only be populated with a single item. A HTTP 400 bad request error will be returned in the response if you specify multiple items. |  [optional] |
|**name** | **String** | A user-defined name of the filter set. Filter set names must be unique globally and match one of the patterns: - &#x60;bidders/_*_/filterSets/_*&#x60; (for accessing bidder-level troubleshooting data) - &#x60;bidders/_*_/accounts/_*_/filterSets/_*&#x60; (for accessing account-level troubleshooting data) This field is required in create operations. |  [optional] |
|**platforms** | [**List&lt;PlatformsEnum&gt;**](#List&lt;PlatformsEnum&gt;) | The list of platforms on which to filter; may be empty. The filters represented by multiple platforms are ORed together (for example, if non-empty, results must match any one of the platforms). |  [optional] |
|**publisherIdentifiers** | **List&lt;String&gt;** | For Open Bidding partners only. The list of publisher identifiers on which to filter; may be empty. The filters represented by multiple publisher identifiers are ORed together. |  [optional] |
|**realtimeTimeRange** | [**RealtimeTimeRange**](RealtimeTimeRange.md) |  |  [optional] |
|**relativeDateRange** | [**RelativeDateRange**](RelativeDateRange.md) |  |  [optional] |
|**sellerNetworkIds** | **List&lt;Integer&gt;** | For Authorized Buyers only. The list of IDs of the seller (publisher) networks on which to filter; may be empty. The filters represented by multiple seller network IDs are ORed together (for example, if non-empty, results must match any one of the publisher networks). See [seller-network-ids](https://developers.google.com/authorized-buyers/rtb/downloads/seller-network-ids) file for the set of existing seller network IDs. |  [optional] |
|**timeSeriesGranularity** | [**TimeSeriesGranularityEnum**](#TimeSeriesGranularityEnum) | The granularity of time intervals if a time series breakdown is preferred; optional. |  [optional] |



## Enum: List&lt;BreakdownDimensionsEnum&gt;

| Name | Value |
|---- | -----|
| BREAKDOWN_DIMENSION_UNSPECIFIED | &quot;BREAKDOWN_DIMENSION_UNSPECIFIED&quot; |
| PUBLISHER_IDENTIFIER | &quot;PUBLISHER_IDENTIFIER&quot; |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| ENVIRONMENT_UNSPECIFIED | &quot;ENVIRONMENT_UNSPECIFIED&quot; |
| WEB | &quot;WEB&quot; |
| APP | &quot;APP&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| FORMAT_UNSPECIFIED | &quot;FORMAT_UNSPECIFIED&quot; |
| NATIVE_DISPLAY | &quot;NATIVE_DISPLAY&quot; |
| NATIVE_VIDEO | &quot;NATIVE_VIDEO&quot; |
| NON_NATIVE_DISPLAY | &quot;NON_NATIVE_DISPLAY&quot; |
| NON_NATIVE_VIDEO | &quot;NON_NATIVE_VIDEO&quot; |



## Enum: List&lt;FormatsEnum&gt;

| Name | Value |
|---- | -----|
| FORMAT_UNSPECIFIED | &quot;FORMAT_UNSPECIFIED&quot; |
| NATIVE_DISPLAY | &quot;NATIVE_DISPLAY&quot; |
| NATIVE_VIDEO | &quot;NATIVE_VIDEO&quot; |
| NON_NATIVE_DISPLAY | &quot;NON_NATIVE_DISPLAY&quot; |
| NON_NATIVE_VIDEO | &quot;NON_NATIVE_VIDEO&quot; |



## Enum: List&lt;PlatformsEnum&gt;

| Name | Value |
|---- | -----|
| PLATFORM_UNSPECIFIED | &quot;PLATFORM_UNSPECIFIED&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| TABLET | &quot;TABLET&quot; |
| MOBILE | &quot;MOBILE&quot; |



## Enum: TimeSeriesGranularityEnum

| Name | Value |
|---- | -----|
| TIME_SERIES_GRANULARITY_UNSPECIFIED | &quot;TIME_SERIES_GRANULARITY_UNSPECIFIED&quot; |
| HOURLY | &quot;HOURLY&quot; |
| DAILY | &quot;DAILY&quot; |



