

# OperationOverrideDTO

Data Transfer object for grouping the mutable properties of an Operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultDelay** | **Integer** | Default delay in milliseconds to apply to mock responses on this operation |  [optional] |
|**dispatcher** | **String** | Type of dispatcher to apply for this operation |  [optional] |
|**dispatcherRules** | **String** | Rules of dispatcher for this operation |  [optional] |
|**parameterConstraints** | [**List&lt;ParameterConstraint&gt;**](ParameterConstraint.md) | Constraints that may apply to incoming parameters on this operation |  [optional] |



