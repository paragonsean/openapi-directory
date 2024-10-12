

# GoogleCloudRecommendationengineV1beta1ImportUserEventsRequest

Request message for the ImportUserEvents request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorsConfig** | [**GoogleCloudRecommendationengineV1beta1ImportErrorsConfig**](GoogleCloudRecommendationengineV1beta1ImportErrorsConfig.md) |  |  [optional] |
|**inputConfig** | [**GoogleCloudRecommendationengineV1beta1InputConfig**](GoogleCloudRecommendationengineV1beta1InputConfig.md) |  |  [optional] |
|**requestId** | **String** | Optional. Unique identifier provided by client, within the ancestor dataset scope. Ensures idempotency for expensive long running operations. Server-generated if unspecified. Up to 128 characters long. This is returned as google.longrunning.Operation.name in the response. Note that this field must not be set if the desired input config is catalog_inline_source. |  [optional] |



