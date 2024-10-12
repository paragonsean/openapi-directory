# InfluxOssApiService.PostQueryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dialect** | [**Dialect**](Dialect.md) |  | [optional] 
**extern** | **File** |  | [optional] 
**now** | **Date** | Specifies the time that should be reported as \&quot;now\&quot; in the query. Default is the server&#39;s now time. | [optional] 
**params** | **{String: Object}** | Enumeration of key/value pairs that respresent parameters to be injected into query (can only specify either this field or extern and not both)  | [optional] 
**query** | **String** | InfluxQL query execute. | 
**type** | **String** | The type of query. Must be \&quot;flux\&quot;. | [optional] 
**bucket** | **String** | Bucket is to be used instead of the database and retention policy specified in the InfluxQL query. | [optional] 



## Enum: TypeEnum


* `flux` (value: `"flux"`)

* `influxql` (value: `"influxql"`)




