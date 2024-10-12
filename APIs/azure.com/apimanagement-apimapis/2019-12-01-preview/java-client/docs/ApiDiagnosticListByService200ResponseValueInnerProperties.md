

# ApiDiagnosticListByService200ResponseValueInnerProperties

Diagnostic Entity Properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alwaysLog** | [**AlwaysLogEnum**](#AlwaysLogEnum) | Specifies for what type of messages sampling settings should not apply. |  [optional] |
|**backend** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend**](ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend.md) |  |  [optional] |
|**frontend** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend**](ApiDiagnosticListByService200ResponseValueInnerPropertiesBackend.md) |  |  [optional] |
|**httpCorrelationProtocol** | [**HttpCorrelationProtocolEnum**](#HttpCorrelationProtocolEnum) | Sets correlation protocol to use for Application Insights diagnostics. |  [optional] |
|**logClientIp** | **Boolean** | Log the ClientIP. Default is false. |  [optional] |
|**loggerId** | **String** | Resource Id of a target logger. |  |
|**sampling** | [**ApiDiagnosticListByService200ResponseValueInnerPropertiesSampling**](ApiDiagnosticListByService200ResponseValueInnerPropertiesSampling.md) |  |  [optional] |
|**verbosity** | [**VerbosityEnum**](#VerbosityEnum) | The verbosity level applied to traces emitted by trace policies. |  [optional] |



## Enum: AlwaysLogEnum

| Name | Value |
|---- | -----|
| ALL_ERRORS | &quot;allErrors&quot; |



## Enum: HttpCorrelationProtocolEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| LEGACY | &quot;Legacy&quot; |
| W3_C | &quot;W3C&quot; |



## Enum: VerbosityEnum

| Name | Value |
|---- | -----|
| VERBOSE | &quot;verbose&quot; |
| INFORMATION | &quot;information&quot; |
| ERROR | &quot;error&quot; |



