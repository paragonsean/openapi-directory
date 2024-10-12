

# ApiDiagnosticListByService200ResponseValueInnerProperties

Diagnostic Entity Properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alwaysLog** | [**AlwaysLogEnum**](#AlwaysLogEnum) | Specifies for what type of messages sampling settings should not apply. |  [optional] |
|**backend** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend**](ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend.md) |  |  [optional] |
|**enableHttpCorrelationHeaders** | **Boolean** | Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true. |  [optional] |
|**frontend** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend**](ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend.md) |  |  [optional] |
|**loggerId** | **String** | Resource Id of a target logger. |  |
|**sampling** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesSampling**](ApiDiagnosticListByService200ResponseValueInnerPropertiesSampling.md) |  |  [optional] |



## Enum: AlwaysLogEnum

| Name | Value |
|---- | -----|
| ALL_ERRORS | &quot;allErrors&quot; |



