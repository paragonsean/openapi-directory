

# GoogleCloudRetailV2alphaExperimentInfoServingConfigExperiment

Metadata for active serving config A/B tests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**experimentServingConfig** | **String** | The fully qualified resource name of the serving config VariantArm.serving_config_id responsible for generating the search response. For example: &#x60;projects/_*_/locations/_*_/catalogs/_*_/servingConfigs/_*&#x60;. |  [optional] |
|**originalServingConfig** | **String** | The fully qualified resource name of the original SearchRequest.placement in the search request prior to reassignment by experiment API. For example: &#x60;projects/_*_/locations/_*_/catalogs/_*_/servingConfigs/_*&#x60;. |  [optional] |



