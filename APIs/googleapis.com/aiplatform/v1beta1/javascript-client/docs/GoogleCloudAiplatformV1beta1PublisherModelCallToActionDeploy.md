# VertexAiApi.GoogleCloudAiplatformV1beta1PublisherModelCallToActionDeploy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactUri** | **String** | Optional. The path to the directory containing the Model artifact and any of its supporting files. | [optional] 
**automaticResources** | [**GoogleCloudAiplatformV1beta1AutomaticResources**](GoogleCloudAiplatformV1beta1AutomaticResources.md) |  | [optional] 
**containerSpec** | [**GoogleCloudAiplatformV1beta1ModelContainerSpec**](GoogleCloudAiplatformV1beta1ModelContainerSpec.md) |  | [optional] 
**dedicatedResources** | [**GoogleCloudAiplatformV1beta1DedicatedResources**](GoogleCloudAiplatformV1beta1DedicatedResources.md) |  | [optional] 
**largeModelReference** | [**GoogleCloudAiplatformV1beta1LargeModelReference**](GoogleCloudAiplatformV1beta1LargeModelReference.md) |  | [optional] 
**modelDisplayName** | **String** | Optional. Default model display name. | [optional] 
**publicArtifactUri** | **String** | Optional. The signed URI for ephemeral Cloud Storage access to model artifact. | [optional] 
**sharedResources** | **String** | The resource name of the shared DeploymentResourcePool to deploy on. Format: &#x60;projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}&#x60; | [optional] 
**title** | **String** | Required. The title of the regional resource reference. | [optional] 


