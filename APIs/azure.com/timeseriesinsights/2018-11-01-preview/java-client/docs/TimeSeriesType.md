

# TimeSeriesType

Time series type defines variables or formulas for doing computation on events associated with time series instances. Each time series instance is associated with exactly one type. A type can have one or more variables. For example, a time series instance might be of type Temperature Sensor, which consists of the variables avg temperature, min temperature, and max temperature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the type. May be null. |  [optional] |
|**id** | **UUID** | Unique type identifier that is immutable. Can be null on create or update requests, and then server generates the ID. Not null on get and delete operations. |  [optional] |
|**name** | **String** | User-given unique name for the type. Mutable, not null. |  |
|**variables** | **Object** | Different variables associated with the type. Not empty, not null. |  |



