# CloudLoggingApi.LogMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketName** | **String** | Optional. The resource name of the Log Bucket that owns the Log Metric. Only Log Buckets in projects are supported. The bucket has to be in the same project as the metric.For example:projects/my-project/locations/global/buckets/my-bucketIf empty, then the Log Metric is considered a non-Bucket Log Metric. | [optional] 
**bucketOptions** | [**BucketOptions**](BucketOptions.md) |  | [optional] 
**createTime** | **String** | Output only. The creation timestamp of the metric.This field may not be present for older metrics. | [optional] [readonly] 
**description** | **String** | Optional. A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters. | [optional] 
**disabled** | **Boolean** | Optional. If set to True, then this metric is disabled and it does not generate any points. | [optional] 
**filter** | **String** | Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced_filters) which is used to match log entries. Example: \&quot;resource.type&#x3D;gae_app AND severity&gt;&#x3D;ERROR\&quot; The maximum length of the filter is 20000 characters. | [optional] 
**labelExtractors** | **{String: String}** | Optional. A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the value_extractor field.The extracted value is converted to the type defined in the label descriptor. If either the extraction or the type conversion fails, the label will have a default value. The default value for a string label is an empty string, for an integer label its 0, and for a boolean label its false.Note that there are upper bounds on the maximum number of labels and the number of active time series that are allowed in a project. | [optional] 
**metricDescriptor** | [**MetricDescriptor**](MetricDescriptor.md) |  | [optional] 
**name** | **String** | Required. The client-assigned metric identifier. Examples: \&quot;error_count\&quot;, \&quot;nginx/requests\&quot;.Metric identifiers are limited to 100 characters and can include only the following characters: A-Z, a-z, 0-9, and the special characters _-.,+!*&#39;,()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.This field is the [METRIC_ID] part of a metric resource name in the format \&quot;projects/PROJECT_ID/metrics/METRIC_ID\&quot;. Example: If the resource name of a metric is \&quot;projects/my-project/metrics/nginx%2Frequests\&quot;, this field&#39;s value is \&quot;nginx/requests\&quot;. | [optional] 
**updateTime** | **String** | Output only. The last update timestamp of the metric.This field may not be present for older metrics. | [optional] [readonly] 
**valueExtractor** | **String** | Optional. A value_extractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction: EXTRACT(field) or REGEXP_EXTRACT(field, regex). The arguments are: field: The name of the log entry field from which the value is to be extracted. regex: A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.The result of the extraction must be convertible to a double type, as the distribution always records double values. If either the extraction or the conversion to double fails, then those values are not recorded in the distribution.Example: REGEXP_EXTRACT(jsonPayload.request, \&quot;.*quantity&#x3D;(\\d+).*\&quot;) | [optional] 
**version** | **String** | Deprecated. The API version that created or updated this metric. The v2 format is used by default and cannot be changed. | [optional] 



## Enum: VersionEnum


* `V2` (value: `"V2"`)

* `V1` (value: `"V1"`)




