

# GoogleCloudAiplatformV1beta1BatchCreateFeaturesRequest

Request message for FeaturestoreService.BatchCreateFeatures.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requests** | [**List&lt;GoogleCloudAiplatformV1beta1CreateFeatureRequest&gt;**](GoogleCloudAiplatformV1beta1CreateFeatureRequest.md) | Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType. The &#x60;parent&#x60; field in each child request message can be omitted. If &#x60;parent&#x60; is set in a child request, then the value must match the &#x60;parent&#x60; value in this request message. |  [optional] |



