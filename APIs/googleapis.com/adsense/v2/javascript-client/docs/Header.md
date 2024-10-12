# AdSenseManagementApi.Header

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyCode** | **String** | The [ISO-4217 currency code](https://en.wikipedia.org/wiki/ISO_4217) of this column. Only present if the header type is METRIC_CURRENCY. | [optional] 
**name** | **String** | Required. Name of the header. | [optional] 
**type** | **String** | Required. Type of the header. | [optional] 



## Enum: TypeEnum


* `HEADER_TYPE_UNSPECIFIED` (value: `"HEADER_TYPE_UNSPECIFIED"`)

* `DIMENSION` (value: `"DIMENSION"`)

* `METRIC_TALLY` (value: `"METRIC_TALLY"`)

* `METRIC_RATIO` (value: `"METRIC_RATIO"`)

* `METRIC_CURRENCY` (value: `"METRIC_CURRENCY"`)

* `METRIC_MILLISECONDS` (value: `"METRIC_MILLISECONDS"`)

* `METRIC_DECIMAL` (value: `"METRIC_DECIMAL"`)




