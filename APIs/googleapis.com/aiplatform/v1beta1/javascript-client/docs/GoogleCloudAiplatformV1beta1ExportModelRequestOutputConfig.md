# VertexAiApi.GoogleCloudAiplatformV1beta1ExportModelRequestOutputConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactDestination** | [**GoogleCloudAiplatformV1beta1GcsDestination**](GoogleCloudAiplatformV1beta1GcsDestination.md) |  | [optional] 
**exportFormatId** | **String** | The ID of the format in which the Model must be exported. Each Model lists the export formats it supports. If no value is provided here, then the first from the list of the Model&#39;s supported formats is used by default. | [optional] 
**imageDestination** | [**GoogleCloudAiplatformV1beta1ContainerRegistryDestination**](GoogleCloudAiplatformV1beta1ContainerRegistryDestination.md) |  | [optional] 


