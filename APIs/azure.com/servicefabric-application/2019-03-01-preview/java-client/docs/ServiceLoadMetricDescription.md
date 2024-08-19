

# ServiceLoadMetricDescription

Specifies a metric to load balance a service during runtime.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultLoad** | **Integer** | Used only for Stateless services. The default amount of load, as a number, that this service creates for this metric. |  [optional] |
|**name** | **String** | The name of the metric. If the service chooses to report load during runtime, the load metric name should match the name that is specified in Name exactly. Note that metric names are case sensitive. |  |
|**primaryDefaultLoad** | **Integer** | Used only for Stateful services. The default amount of load, as a number, that this service creates for this metric when it is a Primary replica. |  [optional] |
|**secondaryDefaultLoad** | **Integer** | Used only for Stateful services. The default amount of load, as a number, that this service creates for this metric when it is a Secondary replica. |  [optional] |
|**weight** | **ServiceLoadMetricWeight** |  |  [optional] |



