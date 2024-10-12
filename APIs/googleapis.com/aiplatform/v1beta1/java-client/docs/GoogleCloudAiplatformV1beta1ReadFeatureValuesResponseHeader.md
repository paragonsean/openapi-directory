

# GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHeader

Response header with metadata for the requested ReadFeatureValuesRequest.entity_type and Features.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityType** | **String** | The resource name of the EntityType from the ReadFeatureValuesRequest. Value format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}&#x60;. |  [optional] |
|**featureDescriptors** | [**List&lt;GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseFeatureDescriptor&gt;**](GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseFeatureDescriptor.md) | List of Feature metadata corresponding to each piece of ReadFeatureValuesResponse.EntityView.data. |  [optional] |



