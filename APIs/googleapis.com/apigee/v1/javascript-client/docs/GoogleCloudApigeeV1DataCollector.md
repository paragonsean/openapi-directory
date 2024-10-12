# ApigeeApi.GoogleCloudApigeeV1DataCollector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **String** | Output only. The time at which the data collector was created in milliseconds since the epoch. | [optional] [readonly] 
**description** | **String** | A description of the data collector. | [optional] 
**lastModifiedAt** | **String** | Output only. The time at which the Data Collector was last updated in milliseconds since the epoch. | [optional] [readonly] 
**name** | **String** | ID of the data collector. Must begin with &#x60;dc_&#x60;. | [optional] 
**type** | **String** | Immutable. The type of data this data collector will collect. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `INTEGER` (value: `"INTEGER"`)

* `FLOAT` (value: `"FLOAT"`)

* `STRING` (value: `"STRING"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `DATETIME` (value: `"DATETIME"`)




