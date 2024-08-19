

# ParameterRanges

<p>Specifies ranges of integer, continuous, and categorical hyperparameters that a hyperparameter tuning job searches. The hyperparameter tuning job launches training jobs with hyperparameter values within these ranges to find the combination of values that result in the training job with the best performance as measured by the objective metric of the hyperparameter tuning job.</p> <note> <p>The maximum number of items specified for <code>Array Members</code> refers to the maximum number of hyperparameters for each range and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of hyperparameters for all the ranges can't exceed the maximum number specified.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**integerParameterRanges** | [**List**](List.md) |  |  [optional] |
|**continuousParameterRanges** | [**List**](List.md) |  |  [optional] |
|**categoricalParameterRanges** | [**List**](List.md) |  |  [optional] |
|**autoParameters** | [**List**](List.md) |  |  [optional] |



