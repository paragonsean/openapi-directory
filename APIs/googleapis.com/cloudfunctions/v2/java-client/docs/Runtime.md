

# Runtime

Describes a runtime and any special information (e.g., deprecation status) related to it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**decommissionDate** | [**Date**](Date.md) |  |  [optional] |
|**deprecationDate** | [**Date**](Date.md) |  |  [optional] |
|**displayName** | **String** | The user facing name, eg &#39;Go 1.13&#39;, &#39;Node.js 12&#39;, etc. |  [optional] |
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | The environment for the runtime. |  [optional] |
|**name** | **String** | The name of the runtime, e.g., &#39;go113&#39;, &#39;nodejs12&#39;, etc. |  [optional] |
|**stage** | [**StageEnum**](#StageEnum) | The stage of life this runtime is in, e.g., BETA, GA, etc. |  [optional] |
|**warnings** | **List&lt;String&gt;** | Warning messages, e.g., a deprecation warning. |  [optional] |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| ENVIRONMENT_UNSPECIFIED | &quot;ENVIRONMENT_UNSPECIFIED&quot; |
| GEN_1 | &quot;GEN_1&quot; |
| GEN_2 | &quot;GEN_2&quot; |



## Enum: StageEnum

| Name | Value |
|---- | -----|
| RUNTIME_STAGE_UNSPECIFIED | &quot;RUNTIME_STAGE_UNSPECIFIED&quot; |
| DEVELOPMENT | &quot;DEVELOPMENT&quot; |
| ALPHA | &quot;ALPHA&quot; |
| BETA | &quot;BETA&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |
| DECOMMISSIONED | &quot;DECOMMISSIONED&quot; |



