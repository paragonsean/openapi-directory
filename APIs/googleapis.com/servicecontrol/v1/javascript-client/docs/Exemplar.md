# ServiceControlApi.Exemplar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **[{String: Object}]** | Contextual information about the example value. Examples are: Trace: type.googleapis.com/google.monitoring.v3.SpanContext Literal string: type.googleapis.com/google.protobuf.StringValue Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system. | [optional] 
**timestamp** | **String** | The observation (sampling) time of the above value. | [optional] 
**value** | **Number** | Value of the exemplar point. This value determines to which bucket the exemplar belongs. | [optional] 


