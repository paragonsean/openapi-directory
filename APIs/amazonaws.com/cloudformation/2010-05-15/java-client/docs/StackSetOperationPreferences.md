

# StackSetOperationPreferences

<p>The user-specified preferences for how CloudFormation performs a stack set operation.</p> <p>For more information about maximum concurrent accounts and failure tolerance, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options\">Stack set operation options</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**regionConcurrencyType** | [**RegionConcurrencyType**](RegionConcurrencyType.md) |  |  [optional] |
|**regionOrder** | [**List**](List.md) |  |  [optional] |
|**failureToleranceCount** | [**Integer**](Integer.md) |  |  [optional] |
|**failureTolerancePercentage** | [**Integer**](Integer.md) |  |  [optional] |
|**maxConcurrentCount** | [**Integer**](Integer.md) |  |  [optional] |
|**maxConcurrentPercentage** | [**Integer**](Integer.md) |  |  [optional] |



