

# DeprecateRule

<p> <b>[AMI policies only]</b> Specifies an AMI deprecation rule for AMIs created by an AMI lifecycle policy.</p> <p>For age-based schedules, you must specify <b>Interval</b> and <b>IntervalUnit</b>. For count-based schedules, you must specify <b>Count</b>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | [**Integer**](Integer.md) |  |  [optional] |
|**interval** | [**Integer**](Integer.md) |  |  [optional] |
|**intervalUnit** | [**RetentionIntervalUnitValues**](RetentionIntervalUnitValues.md) |  |  [optional] |



