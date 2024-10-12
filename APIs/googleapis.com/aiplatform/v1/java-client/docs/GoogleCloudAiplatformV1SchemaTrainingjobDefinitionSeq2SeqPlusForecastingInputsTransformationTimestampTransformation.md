

# GoogleCloudAiplatformV1SchemaTrainingjobDefinitionSeq2SeqPlusForecastingInputsTransformationTimestampTransformation

Training pipeline will perform following transformation functions. * Apply the transformation functions for Numerical columns. * Determine the year, month, day,and weekday. Treat each value from the timestamp as a Categorical column. * Invalid numerical values (for example, values that fall outside of a typical timestamp range, or are extreme values) receive no special treatment and are not removed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnName** | **String** |  |  [optional] |
|**timeFormat** | **String** | The format in which that time field is expressed. The time_format must either be one of: * &#x60;unix-seconds&#x60; * &#x60;unix-milliseconds&#x60; * &#x60;unix-microseconds&#x60; * &#x60;unix-nanoseconds&#x60; (for respectively number of seconds, milliseconds, microseconds and nanoseconds since start of the Unix epoch); or be written in &#x60;strftime&#x60; syntax. If time_format is not set, then the default format is RFC 3339 &#x60;date-time&#x60; format, where &#x60;time-offset&#x60; &#x3D; &#x60;\&quot;Z\&quot;&#x60; (e.g. 1985-04-12T23:20:50.52Z) |  [optional] |



