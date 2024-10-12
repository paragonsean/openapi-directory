

# GoogleCloudMlV1TrialParameter

A message representing a parameter to be tuned. Contains the name of the parameter and the suggested value to use for this trial.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**floatValue** | **Double** | Must be set if ParameterType is DOUBLE or DISCRETE. |  [optional] |
|**intValue** | **String** | Must be set if ParameterType is INTEGER |  [optional] |
|**parameter** | **String** | The name of the parameter. |  [optional] |
|**stringValue** | **String** | Must be set if ParameterTypeis CATEGORICAL |  [optional] |



