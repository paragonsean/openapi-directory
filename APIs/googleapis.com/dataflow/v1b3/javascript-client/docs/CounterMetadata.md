# DataflowApi.CounterMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Human-readable description of the counter semantics. | [optional] 
**kind** | **String** | Counter aggregation kind. | [optional] 
**otherUnits** | **String** | A string referring to the unit type. | [optional] 
**standardUnits** | **String** | System defined Units, see above enum. | [optional] 



## Enum: KindEnum


* `INVALID` (value: `"INVALID"`)

* `SUM` (value: `"SUM"`)

* `MAX` (value: `"MAX"`)

* `MIN` (value: `"MIN"`)

* `MEAN` (value: `"MEAN"`)

* `OR` (value: `"OR"`)

* `AND` (value: `"AND"`)

* `SET` (value: `"SET"`)

* `DISTRIBUTION` (value: `"DISTRIBUTION"`)

* `LATEST_VALUE` (value: `"LATEST_VALUE"`)





## Enum: StandardUnitsEnum


* `BYTES` (value: `"BYTES"`)

* `BYTES_PER_SEC` (value: `"BYTES_PER_SEC"`)

* `MILLISECONDS` (value: `"MILLISECONDS"`)

* `MICROSECONDS` (value: `"MICROSECONDS"`)

* `NANOSECONDS` (value: `"NANOSECONDS"`)

* `TIMESTAMP_MSEC` (value: `"TIMESTAMP_MSEC"`)

* `TIMESTAMP_USEC` (value: `"TIMESTAMP_USEC"`)

* `TIMESTAMP_NSEC` (value: `"TIMESTAMP_NSEC"`)




