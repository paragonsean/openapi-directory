# RecommendationsAiBeta.GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorsConfig** | [**GoogleCloudRecommendationengineV1beta1ImportErrorsConfig**](GoogleCloudRecommendationengineV1beta1ImportErrorsConfig.md) |  | [optional] 
**inputConfig** | [**GoogleCloudRecommendationengineV1beta1InputConfig**](GoogleCloudRecommendationengineV1beta1InputConfig.md) |  | [optional] 
**requestId** | **String** | Optional. Unique identifier provided by client, within the ancestor dataset scope. Ensures idempotency and used for request deduplication. Server-generated if unspecified. Up to 128 characters long. This is returned as google.longrunning.Operation.name in the response. | [optional] 
**updateMask** | **String** | Optional. Indicates which fields in the provided imported &#39;items&#39; to update. If not set, will by default update all fields. | [optional] 


