

# GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericTransformation

Training pipeline will perform following transformation functions. * The value converted to float32. * The z_score of the value. * log(value+1) when the value is greater than or equal to 0. Otherwise, this transformation is not applied and the value is considered a missing value. * z_score of log(value+1) when the value is greater than or equal to 0. Otherwise, this transformation is not applied and the value is considered a missing value. * A boolean value that indicates whether the value is valid.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnName** | **String** |  |  [optional] |
|**invalidValuesAllowed** | **Boolean** | If invalid values is allowed, the training pipeline will create a boolean feature that indicated whether the value is valid. Otherwise, the training pipeline will discard the input row from trainining data. |  [optional] |



