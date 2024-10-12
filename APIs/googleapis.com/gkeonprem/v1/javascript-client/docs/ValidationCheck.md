# AnthosOnPremApi.ValidationCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **String** | Options used for the validation check | [optional] 
**scenario** | **String** | Output only. The scenario when the preflight checks were run. | [optional] [readonly] 
**status** | [**ValidationCheckStatus**](ValidationCheckStatus.md) |  | [optional] 



## Enum: OptionEnum


* `OPTIONS_UNSPECIFIED` (value: `"OPTIONS_UNSPECIFIED"`)

* `SKIP_VALIDATION_CHECK_BLOCKING` (value: `"SKIP_VALIDATION_CHECK_BLOCKING"`)

* `SKIP_VALIDATION_ALL` (value: `"SKIP_VALIDATION_ALL"`)





## Enum: ScenarioEnum


* `SCENARIO_UNSPECIFIED` (value: `"SCENARIO_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `UPDATE` (value: `"UPDATE"`)




