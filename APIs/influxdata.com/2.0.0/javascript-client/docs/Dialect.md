# InfluxOssApiService.Dialect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **[String]** | https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/#columns | [optional] 
**commentPrefix** | **String** | Character prefixed to comment strings | [optional] [default to &#39;#&#39;]
**dateTimeFormat** | **String** | Format of timestamps | [optional] [default to &#39;RFC3339&#39;]
**delimiter** | **String** | Separator between cells; the default is , | [optional] [default to &#39;,&#39;]
**header** | **Boolean** | If true, the results will contain a header row | [optional] [default to true]



## Enum: [AnnotationsEnum]


* `group` (value: `"group"`)

* `datatype` (value: `"datatype"`)

* `default` (value: `"default"`)





## Enum: DateTimeFormatEnum


* `RFC3339` (value: `"RFC3339"`)

* `RFC3339Nano` (value: `"RFC3339Nano"`)




