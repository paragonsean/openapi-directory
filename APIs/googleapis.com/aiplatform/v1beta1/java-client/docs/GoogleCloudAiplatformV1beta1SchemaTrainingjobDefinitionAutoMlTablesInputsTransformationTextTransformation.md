

# GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlTablesInputsTransformationTextTransformation

Training pipeline will perform following transformation functions. * The text as is--no change to case, punctuation, spelling, tense, and so on. * Tokenize text to words. Convert each words to a dictionary lookup index and generate an embedding for each index. Combine the embedding of all elements into a single embedding using the mean. * Tokenization is based on unicode script boundaries. * Missing values get their own lookup index and resulting embedding. * Stop-words receive no special treatment and are not removed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnName** | **String** |  |  [optional] |



