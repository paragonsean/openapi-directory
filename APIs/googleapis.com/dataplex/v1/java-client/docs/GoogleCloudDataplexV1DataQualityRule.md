

# GoogleCloudDataplexV1DataQualityRule

A rule captures data quality intent about a data source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**column** | **String** | Optional. The unnested column which this rule is evaluated against. |  [optional] |
|**description** | **String** | Optional. Description of the rule. The maximum length is 1,024 characters. |  [optional] |
|**dimension** | **String** | Required. The dimension a rule belongs to. Results are also aggregated at the dimension level. Supported dimensions are \&quot;COMPLETENESS\&quot;, \&quot;ACCURACY\&quot;, \&quot;CONSISTENCY\&quot;, \&quot;VALIDITY\&quot;, \&quot;UNIQUENESS\&quot;, \&quot;INTEGRITY\&quot; |  [optional] |
|**ignoreNull** | **Boolean** | Optional. Rows with null values will automatically fail a rule, unless ignore_null is true. In that case, such null rows are trivially considered passing.This field is only valid for the following type of rules: RangeExpectation RegexExpectation SetExpectation UniquenessExpectation |  [optional] |
|**name** | **String** | Optional. A mutable name for the rule. The name must contain only letters (a-z, A-Z), numbers (0-9), or hyphens (-). The maximum length is 63 characters. Must start with a letter. Must end with a number or a letter. |  [optional] |
|**nonNullExpectation** | **Object** | Evaluates whether each column value is null. |  [optional] |
|**rangeExpectation** | [**GoogleCloudDataplexV1DataQualityRuleRangeExpectation**](GoogleCloudDataplexV1DataQualityRuleRangeExpectation.md) |  |  [optional] |
|**regexExpectation** | [**GoogleCloudDataplexV1DataQualityRuleRegexExpectation**](GoogleCloudDataplexV1DataQualityRuleRegexExpectation.md) |  |  [optional] |
|**rowConditionExpectation** | [**GoogleCloudDataplexV1DataQualityRuleRowConditionExpectation**](GoogleCloudDataplexV1DataQualityRuleRowConditionExpectation.md) |  |  [optional] |
|**setExpectation** | [**GoogleCloudDataplexV1DataQualityRuleSetExpectation**](GoogleCloudDataplexV1DataQualityRuleSetExpectation.md) |  |  [optional] |
|**statisticRangeExpectation** | [**GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectation**](GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectation.md) |  |  [optional] |
|**tableConditionExpectation** | [**GoogleCloudDataplexV1DataQualityRuleTableConditionExpectation**](GoogleCloudDataplexV1DataQualityRuleTableConditionExpectation.md) |  |  [optional] |
|**threshold** | **Double** | Optional. The minimum ratio of passing_rows / total_rows required to pass this rule, with a range of 0.0, 1.0.0 indicates default value (i.e. 1.0).This field is only valid for row-level type rules. |  [optional] |
|**uniquenessExpectation** | **Object** | Evaluates whether the column has duplicates. |  [optional] |



