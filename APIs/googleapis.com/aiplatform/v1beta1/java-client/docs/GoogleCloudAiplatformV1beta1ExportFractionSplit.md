

# GoogleCloudAiplatformV1beta1ExportFractionSplit

Assigns the input data to training, validation, and test sets as per the given fractions. Any of `training_fraction`, `validation_fraction` and `test_fraction` may optionally be provided, they must sum to up to 1. If the provided ones sum to less than 1, the remainder is assigned to sets as decided by Vertex AI. If none of the fractions are set, by default roughly 80% of data is used for training, 10% for validation, and 10% for test.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**testFraction** | **Double** | The fraction of the input data that is to be used to evaluate the Model. |  [optional] |
|**trainingFraction** | **Double** | The fraction of the input data that is to be used to train the Model. |  [optional] |
|**validationFraction** | **Double** | The fraction of the input data that is to be used to validate the Model. |  [optional] |



