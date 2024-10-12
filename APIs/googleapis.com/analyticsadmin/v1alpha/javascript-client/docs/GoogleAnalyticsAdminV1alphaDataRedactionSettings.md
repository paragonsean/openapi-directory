# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaDataRedactionSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailRedactionEnabled** | **Boolean** | If enabled, any event parameter or user property values that look like an email will be redacted. | [optional] 
**name** | **String** | Output only. Name of this Data Redaction Settings resource. Format: properties/{property_id}/dataStreams/{data_stream}/dataRedactionSettings Example: \&quot;properties/1000/dataStreams/2000/dataRedactionSettings\&quot; | [optional] [readonly] 
**queryParameterKeys** | **[String]** | The query parameter keys to apply redaction logic to if present in the URL. Query parameter matching is case-insensitive. Must contain at least one element if query_parameter_replacement_enabled is true. Keys cannot contain commas. | [optional] 
**queryParameterRedactionEnabled** | **Boolean** | Query Parameter redaction removes the key and value portions of a query parameter if it is in the configured set of query parameters. If enabled, URL query replacement logic will be run for the Stream. Any query parameters defined in query_parameter_keys will be redacted. | [optional] 


