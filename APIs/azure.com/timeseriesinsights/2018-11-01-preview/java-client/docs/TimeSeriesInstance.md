

# TimeSeriesInstance

Time series instances are the time series themselves. In most cases, the deviceId or assetId is the unique identifier of the asset in the environment. Instances have descriptive information associated with them called instance fields. At a minimum, instance fields include hierarchy information. They can also include useful, descriptive data like the manufacturer, operator, or the last service date.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | This optional field contains description about the instance. |  [optional] |
|**hierarchyIds** | **List&lt;UUID&gt;** | Set of time series hierarchy IDs that the instance belong to. May be null. |  [optional] |
|**instanceFields** | **Map&lt;String, Object&gt;** | Set of key-value pairs that contain user-defined instance properties. May be null. |  [optional] |
|**name** | **String** | Optional name of the instance which is unique in an environment. Names acts as a mutable alias or display name of the time series instance. Mutable, may be null. |  [optional] |
|**timeSeriesId** | **List&lt;Object&gt;** | A single Time Series ID value that is an array of primitive values that uniquely identifies a time series instance (e.g. a single device). Note that a single Time Series ID can be composite if multiple properties are specified as Time Series ID at environment creation time. The position and type of values must match Time Series ID properties specified on the environment and returned by Get Model Setting API. Cannot be empty. |  |
|**typeId** | **UUID** | This represents the type that this instance belongs to. Never null. |  |



