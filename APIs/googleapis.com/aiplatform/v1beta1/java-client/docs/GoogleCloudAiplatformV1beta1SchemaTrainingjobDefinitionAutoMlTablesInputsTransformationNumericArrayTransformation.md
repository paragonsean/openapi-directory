

# GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationNumericArrayTransformation

Treats the column as numerical array and performs following transformation functions. * All transformations for Numerical types applied to the average of the all elements. * The average of empty arrays is treated as zero.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnName** | **String** |  |  [optional] |
|**invalidValuesAllowed** | **Boolean** | If invalid values is allowed, the training pipeline will create a boolean feature that indicated whether the value is valid. Otherwise, the training pipeline will discard the input row from trainining data. |  [optional] |



