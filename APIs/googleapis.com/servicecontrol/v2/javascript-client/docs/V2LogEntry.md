# ServiceControlApi.V2LogEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**httpRequest** | [**V2HttpRequest**](V2HttpRequest.md) |  | [optional] 
**insertId** | **String** | A unique ID for the log entry used for deduplication. If omitted, the implementation will generate one based on operation_id. | [optional] 
**labels** | **{String: String}** | A set of user-defined (key, value) data that provides additional information about the log entry. | [optional] 
**monitoredResourceLabels** | **{String: String}** | A set of user-defined (key, value) data that provides additional information about the moniotored resource that the log entry belongs to. | [optional] 
**name** | **String** | Required. The log to which this log entry belongs. Examples: &#x60;\&quot;syslog\&quot;&#x60;, &#x60;\&quot;book_log\&quot;&#x60;. | [optional] 
**operation** | [**V2LogEntryOperation**](V2LogEntryOperation.md) |  | [optional] 
**protoPayload** | **{String: Object}** | The log entry payload, represented as a protocol buffer that is expressed as a JSON object. The only accepted type currently is AuditLog. | [optional] 
**severity** | **String** | The severity of the log entry. The default value is &#x60;LogSeverity.DEFAULT&#x60;. | [optional] 
**sourceLocation** | [**V2LogEntrySourceLocation**](V2LogEntrySourceLocation.md) |  | [optional] 
**structPayload** | **{String: Object}** | The log entry payload, represented as a structure that is expressed as a JSON object. | [optional] 
**textPayload** | **String** | The log entry payload, represented as a Unicode string (UTF-8). | [optional] 
**timestamp** | **String** | The time the event described by the log entry occurred. If omitted, defaults to operation start time. | [optional] 
**trace** | **String** | Optional. Resource name of the trace associated with the log entry, if any. If this field contains a relative resource name, you can assume the name is relative to &#x60;//tracing.googleapis.com&#x60;. Example: &#x60;projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824&#x60; | [optional] 



## Enum: SeverityEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `DEBUG` (value: `"DEBUG"`)

* `INFO` (value: `"INFO"`)

* `NOTICE` (value: `"NOTICE"`)

* `WARNING` (value: `"WARNING"`)

* `ERROR` (value: `"ERROR"`)

* `CRITICAL` (value: `"CRITICAL"`)

* `ALERT` (value: `"ALERT"`)

* `EMERGENCY` (value: `"EMERGENCY"`)




