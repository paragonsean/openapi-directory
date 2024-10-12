

# DiagnosticsDescription

Describes the diagnostics options available

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultSinkRefs** | **List&lt;String&gt;** | The sinks to be used if diagnostics is enabled. Sink choices can be overridden at the service and code package level. |  [optional] |
|**enabled** | **Boolean** | Status of whether or not sinks are enabled. |  [optional] |
|**sinks** | [**List&lt;DiagnosticsSinkProperties&gt;**](DiagnosticsSinkProperties.md) | List of supported sinks that can be referenced. |  [optional] |



