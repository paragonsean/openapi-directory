# CloudFunctionsApi.Runtime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decommissionDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**deprecationDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**displayName** | **String** | The user facing name, eg &#39;Go 1.13&#39;, &#39;Node.js 12&#39;, etc. | [optional] 
**environment** | **String** | The environment for the runtime. | [optional] 
**name** | **String** | The name of the runtime, e.g., &#39;go113&#39;, &#39;nodejs12&#39;, etc. | [optional] 
**stage** | **String** | The stage of life this runtime is in, e.g., BETA, GA, etc. | [optional] 
**warnings** | **[String]** | Warning messages, e.g., a deprecation warning. | [optional] 



## Enum: EnvironmentEnum


* `ENVIRONMENT_UNSPECIFIED` (value: `"ENVIRONMENT_UNSPECIFIED"`)

* `GEN_1` (value: `"GEN_1"`)

* `GEN_2` (value: `"GEN_2"`)





## Enum: StageEnum


* `RUNTIME_STAGE_UNSPECIFIED` (value: `"RUNTIME_STAGE_UNSPECIFIED"`)

* `DEVELOPMENT` (value: `"DEVELOPMENT"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)

* `DECOMMISSIONED` (value: `"DECOMMISSIONED"`)




