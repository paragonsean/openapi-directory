

# CounterUpdate

An update to a Counter sent from a worker.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_boolean** | **Boolean** | Boolean value for And, Or. |  [optional] |
|**cumulative** | **Boolean** | True if this counter is reported as the total cumulative aggregate value accumulated since the worker started working on this WorkItem. By default this is false, indicating that this counter is reported as a delta. |  [optional] |
|**distribution** | [**DistributionUpdate**](DistributionUpdate.md) |  |  [optional] |
|**floatingPoint** | **Double** | Floating point value for Sum, Max, Min. |  [optional] |
|**floatingPointList** | [**FloatingPointList**](FloatingPointList.md) |  |  [optional] |
|**floatingPointMean** | [**FloatingPointMean**](FloatingPointMean.md) |  |  [optional] |
|**integer** | [**SplitInt64**](SplitInt64.md) |  |  [optional] |
|**integerGauge** | [**IntegerGauge**](IntegerGauge.md) |  |  [optional] |
|**integerList** | [**IntegerList**](IntegerList.md) |  |  [optional] |
|**integerMean** | [**IntegerMean**](IntegerMean.md) |  |  [optional] |
|**internal** | **Object** | Value for internally-defined counters used by the Dataflow service. |  [optional] |
|**nameAndKind** | [**NameAndKind**](NameAndKind.md) |  |  [optional] |
|**shortId** | **String** | The service-generated short identifier for this counter. The short_id -&gt; (name, metadata) mapping is constant for the lifetime of a job. |  [optional] |
|**stringList** | [**StringList**](StringList.md) |  |  [optional] |
|**structuredNameAndMetadata** | [**CounterStructuredNameAndMetadata**](CounterStructuredNameAndMetadata.md) |  |  [optional] |



