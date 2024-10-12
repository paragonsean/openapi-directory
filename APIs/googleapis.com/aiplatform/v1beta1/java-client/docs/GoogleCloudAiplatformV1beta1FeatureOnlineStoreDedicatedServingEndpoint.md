

# GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpoint

The dedicated serving endpoint for this FeatureOnlineStore. Only need to set when you choose Optimized storage type or enable EmbeddingManagement. Will use public endpoint by default. Note, for EmbeddingManagement use case, only [DedicatedServingEndpoint.public_endpoint_domain_name] is available now.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateServiceConnectConfig** | [**GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig**](GoogleCloudAiplatformV1beta1PrivateServiceConnectConfig.md) |  |  [optional] |
|**publicEndpointDomainName** | **String** | Output only. This field will be populated with the domain name to use for this FeatureOnlineStore |  [optional] [readonly] |
|**serviceAttachment** | **String** | Output only. The name of the service attachment resource. Populated if private service connect is enabled and after FeatureViewSync is created. |  [optional] [readonly] |



