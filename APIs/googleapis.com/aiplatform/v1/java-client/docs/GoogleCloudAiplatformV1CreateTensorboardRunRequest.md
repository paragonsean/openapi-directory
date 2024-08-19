

# GoogleCloudAiplatformV1CreateTensorboardRunRequest

Request message for TensorboardService.CreateTensorboardRun.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parent** | **String** | Required. The resource name of the TensorboardExperiment to create the TensorboardRun in. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; |  [optional] |
|**tensorboardRun** | [**GoogleCloudAiplatformV1TensorboardRun**](GoogleCloudAiplatformV1TensorboardRun.md) |  |  [optional] |
|**tensorboardRunId** | **String** | Required. The ID to use for the Tensorboard run, which becomes the final component of the Tensorboard run&#39;s resource name. This value should be 1-128 characters, and valid characters are &#x60;/a-z-/&#x60;. |  [optional] |



