

# GoogleCloudDataplexV1DataQualityScanRuleResult

Information about the result of a data quality rule for data quality scan. The monitored resource is 'DataScan'.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**column** | **String** | The column which this rule is evaluated against. |  [optional] |
|**dataSource** | **String** | The data source of the data scan (e.g. BigQuery table name). |  [optional] |
|**evaluatedRowCount** | **String** | The number of rows evaluated against the data quality rule. This field is only valid for rules of PER_ROW evaluation type. |  [optional] |
|**evalutionType** | [**EvalutionTypeEnum**](#EvalutionTypeEnum) | The evaluation type of the data quality rule. |  [optional] |
|**jobId** | **String** | Identifier of the specific data scan job this log entry is for. |  [optional] |
|**nullRowCount** | **String** | The number of rows with null values in the specified column. |  [optional] |
|**passedRowCount** | **String** | The number of rows which passed a rule evaluation. This field is only valid for rules of PER_ROW evaluation type. |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | The result of the data quality rule. |  [optional] |
|**ruleDimension** | **String** | The dimension of the data quality rule. |  [optional] |
|**ruleName** | **String** | The name of the data quality rule. |  [optional] |
|**ruleType** | [**RuleTypeEnum**](#RuleTypeEnum) | The type of the data quality rule. |  [optional] |
|**thresholdPercent** | **Double** | The passing threshold (0.0, 100.0) of the data quality rule. |  [optional] |



## Enum: EvalutionTypeEnum

| Name | Value |
|---- | -----|
| EVALUATION_TYPE_UNSPECIFIED | &quot;EVALUATION_TYPE_UNSPECIFIED&quot; |
| PER_ROW | &quot;PER_ROW&quot; |
| AGGREGATE | &quot;AGGREGATE&quot; |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| RESULT_UNSPECIFIED | &quot;RESULT_UNSPECIFIED&quot; |
| PASSED | &quot;PASSED&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: RuleTypeEnum

| Name | Value |
|---- | -----|
| RULE_TYPE_UNSPECIFIED | &quot;RULE_TYPE_UNSPECIFIED&quot; |
| NON_NULL_EXPECTATION | &quot;NON_NULL_EXPECTATION&quot; |
| RANGE_EXPECTATION | &quot;RANGE_EXPECTATION&quot; |
| REGEX_EXPECTATION | &quot;REGEX_EXPECTATION&quot; |
| ROW_CONDITION_EXPECTATION | &quot;ROW_CONDITION_EXPECTATION&quot; |
| SET_EXPECTATION | &quot;SET_EXPECTATION&quot; |
| STATISTIC_RANGE_EXPECTATION | &quot;STATISTIC_RANGE_EXPECTATION&quot; |
| TABLE_CONDITION_EXPECTATION | &quot;TABLE_CONDITION_EXPECTATION&quot; |
| UNIQUENESS_EXPECTATION | &quot;UNIQUENESS_EXPECTATION&quot; |



