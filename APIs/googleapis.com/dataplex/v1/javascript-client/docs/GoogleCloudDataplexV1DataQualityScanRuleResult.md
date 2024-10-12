# CloudDataplexApi.GoogleCloudDataplexV1DataQualityScanRuleResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **String** | The column which this rule is evaluated against. | [optional] 
**dataSource** | **String** | The data source of the data scan (e.g. BigQuery table name). | [optional] 
**evaluatedRowCount** | **String** | The number of rows evaluated against the data quality rule. This field is only valid for rules of PER_ROW evaluation type. | [optional] 
**evalutionType** | **String** | The evaluation type of the data quality rule. | [optional] 
**jobId** | **String** | Identifier of the specific data scan job this log entry is for. | [optional] 
**nullRowCount** | **String** | The number of rows with null values in the specified column. | [optional] 
**passedRowCount** | **String** | The number of rows which passed a rule evaluation. This field is only valid for rules of PER_ROW evaluation type. | [optional] 
**result** | **String** | The result of the data quality rule. | [optional] 
**ruleDimension** | **String** | The dimension of the data quality rule. | [optional] 
**ruleName** | **String** | The name of the data quality rule. | [optional] 
**ruleType** | **String** | The type of the data quality rule. | [optional] 
**thresholdPercent** | **Number** | The passing threshold (0.0, 100.0) of the data quality rule. | [optional] 



## Enum: EvalutionTypeEnum


* `EVALUATION_TYPE_UNSPECIFIED` (value: `"EVALUATION_TYPE_UNSPECIFIED"`)

* `PER_ROW` (value: `"PER_ROW"`)

* `AGGREGATE` (value: `"AGGREGATE"`)





## Enum: ResultEnum


* `RESULT_UNSPECIFIED` (value: `"RESULT_UNSPECIFIED"`)

* `PASSED` (value: `"PASSED"`)

* `FAILED` (value: `"FAILED"`)





## Enum: RuleTypeEnum


* `RULE_TYPE_UNSPECIFIED` (value: `"RULE_TYPE_UNSPECIFIED"`)

* `NON_NULL_EXPECTATION` (value: `"NON_NULL_EXPECTATION"`)

* `RANGE_EXPECTATION` (value: `"RANGE_EXPECTATION"`)

* `REGEX_EXPECTATION` (value: `"REGEX_EXPECTATION"`)

* `ROW_CONDITION_EXPECTATION` (value: `"ROW_CONDITION_EXPECTATION"`)

* `SET_EXPECTATION` (value: `"SET_EXPECTATION"`)

* `STATISTIC_RANGE_EXPECTATION` (value: `"STATISTIC_RANGE_EXPECTATION"`)

* `TABLE_CONDITION_EXPECTATION` (value: `"TABLE_CONDITION_EXPECTATION"`)

* `UNIQUENESS_EXPECTATION` (value: `"UNIQUENESS_EXPECTATION"`)




