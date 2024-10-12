

# PostQueryRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dialect** | [**Dialect**](Dialect.md) |  |  [optional] |
|**extern** | [**ModelFile**](ModelFile.md) |  |  [optional] |
|**now** | **OffsetDateTime** | Specifies the time that should be reported as \&quot;now\&quot; in the query. Default is the server&#39;s now time. |  [optional] |
|**params** | **Map&lt;String, Object&gt;** | Enumeration of key/value pairs that respresent parameters to be injected into query (can only specify either this field or extern and not both)  |  [optional] |
|**query** | **String** | InfluxQL query execute. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of query. Must be \&quot;flux\&quot;. |  [optional] |
|**bucket** | **String** | Bucket is to be used instead of the database and retention policy specified in the InfluxQL query. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FLUX | &quot;flux&quot; |
| INFLUXQL | &quot;influxql&quot; |



