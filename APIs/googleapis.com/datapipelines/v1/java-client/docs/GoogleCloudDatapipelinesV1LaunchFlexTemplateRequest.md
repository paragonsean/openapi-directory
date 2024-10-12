

# GoogleCloudDatapipelinesV1LaunchFlexTemplateRequest

A request to launch a Dataflow job from a Flex Template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**launchParameter** | [**GoogleCloudDatapipelinesV1LaunchFlexTemplateParameter**](GoogleCloudDatapipelinesV1LaunchFlexTemplateParameter.md) |  |  [optional] |
|**location** | **String** | Required. The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request. For example, &#x60;us-central1&#x60;, &#x60;us-west1&#x60;. |  [optional] |
|**projectId** | **String** | Required. The ID of the Cloud Platform project that the job belongs to. |  [optional] |
|**validateOnly** | **Boolean** | If true, the request is validated but not actually executed. Defaults to false. |  [optional] |



