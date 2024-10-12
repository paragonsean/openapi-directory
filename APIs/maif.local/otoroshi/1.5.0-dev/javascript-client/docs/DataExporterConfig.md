# OtoroshiAdminApi.DataExporterConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bufferSize** | **Number** | buffer size | [optional] 
**config** | [**DataExporterConfigConfig**](DataExporterConfigConfig.md) |  | [optional] 
**desc** | **String** | Description | [optional] 
**enabled** | **String** | Boolean | [optional] 
**filtering** | [**Filtering**](Filtering.md) |  | [optional] 
**groupDuration** | **Number** | duration | [optional] 
**groupSize** | **Number** | Group size | [optional] 
**id** | **String** | Id | [optional] 
**jsonWorkers** | **Number** | nb workers | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**metadata** | **{String: String}** | Metadata | [optional] 
**name** | **String** | Name | [optional] 
**projection** | **{String: String}** | projection | [optional] 
**sendWorkers** | **Number** | send workers | [optional] 
**typ** | **String** | Type of data exporter | [optional] 



## Enum: TypEnum


* `kafka` (value: `"kafka"`)

* `pulsar` (value: `"pulsar"`)

* `file` (value: `"file"`)

* `mailer` (value: `"mailer"`)

* `elastic` (value: `"elastic"`)

* `console` (value: `"console"`)

* `custom` (value: `"custom"`)




