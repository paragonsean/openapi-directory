

# GoogleCloudAiplatformV1PurgeContextsResponse

Response message for MetadataService.PurgeContexts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**purgeCount** | **String** | The number of Contexts that this request deleted (or, if &#x60;force&#x60; is false, the number of Contexts that will be deleted). This can be an estimate. |  [optional] |
|**purgeSample** | **List&lt;String&gt;** | A sample of the Context names that will be deleted. Only populated if &#x60;force&#x60; is set to false. The maximum number of samples is 100 (it is possible to return fewer). |  [optional] |



