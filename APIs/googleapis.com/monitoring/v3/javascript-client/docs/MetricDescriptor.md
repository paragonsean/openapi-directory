# CloudMonitoringApi.MetricDescriptor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A detailed description of the metric, which can be used in documentation. | [optional] 
**displayName** | **String** | A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example \&quot;Request count\&quot;. This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota. | [optional] 
**labels** | [**[LabelDescriptor]**](LabelDescriptor.md) | The set of labels that can be used to describe a specific instance of this metric type. For example, the appengine.googleapis.com/http/server/response_latencies metric type has a label for the HTTP response code, response_code, so you can look at latencies for successful responses or just for responses that failed. | [optional] 
**launchStage** | **String** | Optional. The launch stage of the metric definition. | [optional] 
**metadata** | [**MetricDescriptorMetadata**](MetricDescriptorMetadata.md) |  | [optional] 
**metricKind** | **String** | Whether the metric records instantaneous values, changes to a value, etc. Some combinations of metric_kind and value_type might not be supported. | [optional] 
**monitoredResourceTypes** | **[String]** | Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here. | [optional] 
**name** | **String** | The resource name of the metric descriptor. | [optional] 
**type** | **String** | The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name custom.googleapis.com or external.googleapis.com. Metric types should use a natural hierarchical grouping. For example: \&quot;custom.googleapis.com/invoice/paid/amount\&quot; \&quot;external.googleapis.com/prometheus/up\&quot; \&quot;appengine.googleapis.com/http/server/response_latencies\&quot;  | [optional] 
**unit** | **String** | The units in which the metric value is reported. It is only applicable if the value_type is INT64, DOUBLE, or DISTRIBUTION. The unit defines the representation of the stored metric values.Different systems might scale the values to be more easily displayed (so a value of 0.02kBy might be displayed as 20By, and a value of 3523kBy might be displayed as 3.5MBy). However, if the unit is kBy, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an INT64 CUMULATIVE metric whose unit is s{CPU} (or equivalently 1s{CPU} or just s). If the job uses 12,005 CPU-seconds, then the value is written as 12005.Alternatively, if you want a custom metric to record data in a more granular way, you can create a DOUBLE CUMULATIVE metric whose unit is ks{CPU}, and then write the value 12.005 (which is 12005/1000), or use Kis{CPU} and write 11.723 (which is 12005/1024).The supported units are a subset of The Unified Code for Units of Measure (https://unitsofmeasure.org/ucum.html) standard:Basic units (UNIT) bit bit By byte s second min minute h hour d day 1 dimensionlessPrefixes (PREFIX) k kilo (10^3) M mega (10^6) G giga (10^9) T tera (10^12) P peta (10^15) E exa (10^18) Z zetta (10^21) Y yotta (10^24) m milli (10^-3) u micro (10^-6) n nano (10^-9) p pico (10^-12) f femto (10^-15) a atto (10^-18) z zepto (10^-21) y yocto (10^-24) Ki kibi (2^10) Mi mebi (2^20) Gi gibi (2^30) Ti tebi (2^40) Pi pebi (2^50)GrammarThe grammar also includes these connectors: / division or ratio (as an infix operator). For examples, kBy/{email} or MiBy/10ms (although you should almost never have /s in a metric unit; rates should always be computed at query time from the underlying cumulative or delta value). . multiplication or composition (as an infix operator). For examples, GBy.d or k{watt}.h.The grammar for a unit is as follows: Expression &#x3D; Component { \&quot;.\&quot; Component } { \&quot;/\&quot; Component } ; Component &#x3D; ( [ PREFIX ] UNIT | \&quot;%\&quot; ) [ Annotation ] | Annotation | \&quot;1\&quot; ; Annotation &#x3D; \&quot;{\&quot; NAME \&quot;}\&quot; ; Notes: Annotation is just a comment if it follows a UNIT. If the annotation is used alone, then the unit is equivalent to 1. For examples, {request}/s &#x3D;&#x3D; 1/s, By{transmitted}/s &#x3D;&#x3D; By/s. NAME is a sequence of non-blank printable ASCII characters not containing { or }. 1 represents a unitary dimensionless unit (https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in 1/s. It is typically used when none of the basic units are appropriate. For example, \&quot;new users per day\&quot; can be represented as 1/d or {new-users}/d (and a metric value 5 would mean \&quot;5 new users). Alternatively, \&quot;thousands of page views per day\&quot; would be represented as 1000/d or k1/d or k{page_views}/d (and a metric value of 5.3 would mean \&quot;5300 page views per day\&quot;). % represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value 3 means \&quot;3 percent\&quot;). 10^2.% indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value 0.03 means \&quot;3 percent\&quot;). | [optional] 
**valueType** | **String** | Whether the measurement is an integer, a floating-point number, etc. Some combinations of metric_kind and value_type might not be supported. | [optional] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `PRELAUNCH` (value: `"PRELAUNCH"`)

* `EARLY_ACCESS` (value: `"EARLY_ACCESS"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)





## Enum: MetricKindEnum


* `METRIC_KIND_UNSPECIFIED` (value: `"METRIC_KIND_UNSPECIFIED"`)

* `GAUGE` (value: `"GAUGE"`)

* `DELTA` (value: `"DELTA"`)

* `CUMULATIVE` (value: `"CUMULATIVE"`)





## Enum: ValueTypeEnum


* `VALUE_TYPE_UNSPECIFIED` (value: `"VALUE_TYPE_UNSPECIFIED"`)

* `BOOL` (value: `"BOOL"`)

* `INT64` (value: `"INT64"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `STRING` (value: `"STRING"`)

* `DISTRIBUTION` (value: `"DISTRIBUTION"`)

* `MONEY` (value: `"MONEY"`)




