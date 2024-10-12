

# GoogleCloudAiplatformV1PublisherModelCallToActionDeploy

Model metadata that is needed for UploadModel or DeployModel/CreateEndpoint requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactUri** | **String** | Optional. The path to the directory containing the Model artifact and any of its supporting files. |  [optional] |
|**automaticResources** | [**GoogleCloudAiplatformV1AutomaticResources**](GoogleCloudAiplatformV1AutomaticResources.md) |  |  [optional] |
|**containerSpec** | [**GoogleCloudAiplatformV1ModelContainerSpec**](GoogleCloudAiplatformV1ModelContainerSpec.md) |  |  [optional] |
|**dedicatedResources** | [**GoogleCloudAiplatformV1DedicatedResources**](GoogleCloudAiplatformV1DedicatedResources.md) |  |  [optional] |
|**largeModelReference** | [**GoogleCloudAiplatformV1LargeModelReference**](GoogleCloudAiplatformV1LargeModelReference.md) |  |  [optional] |
|**modelDisplayName** | **String** | Optional. Default model display name. |  [optional] |
|**publicArtifactUri** | **String** | Optional. The signed URI for ephemeral Cloud Storage access to model artifact. |  [optional] |
|**sharedResources** | **String** | The resource name of the shared DeploymentResourcePool to deploy on. Format: &#x60;projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}&#x60; |  [optional] |
|**title** | **String** | Required. The title of the regional resource reference. |  [optional] |



