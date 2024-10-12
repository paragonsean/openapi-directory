

# InfluxQLQuery

Query influx using the InfluxQL language

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucket** | **String** | Bucket is to be used instead of the database and retention policy specified in the InfluxQL query. |  [optional] |
|**query** | **String** | InfluxQL query execute. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of query. Must be \&quot;influxql\&quot;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INFLUXQL | &quot;influxql&quot; |



