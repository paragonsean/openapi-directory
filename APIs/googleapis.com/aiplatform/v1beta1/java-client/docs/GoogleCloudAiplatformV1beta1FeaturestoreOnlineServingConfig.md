

# GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfig

OnlineServingConfig specifies the details for provisioning online serving resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fixedNodeCount** | **Integer** | The number of nodes for the online store. The number of nodes doesn&#39;t scale automatically, but you can manually update the number of nodes. If set to 0, the featurestore will not have an online store and cannot be used for online serving. |  [optional] |
|**scaling** | [**GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling**](GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling.md) |  |  [optional] |



