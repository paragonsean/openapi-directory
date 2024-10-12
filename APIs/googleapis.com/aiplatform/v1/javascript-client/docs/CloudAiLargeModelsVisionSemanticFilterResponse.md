# VertexAiApi.CloudAiLargeModelsVisionSemanticFilterResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namedBoundingBoxes** | [**[CloudAiLargeModelsVisionNamedBoundingBox]**](CloudAiLargeModelsVisionNamedBoundingBox.md) | Class labels of the bounding boxes that failed the semantic filtering. Bounding box coordinates. | [optional] 
**passedSemanticFilter** | **Boolean** | This response is added when semantic filter config is turned on in EditConfig. It reports if this image is passed semantic filter response. If passed_semantic_filter is false, the bounding box information will be populated for user to check what caused the semantic filter to fail. | [optional] 


