

# GoogleCloudAiplatformV1beta1PurgeExecutionsResponse

Response message for MetadataService.PurgeExecutions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**purgeCount** | **String** | The number of Executions that this request deleted (or, if &#x60;force&#x60; is false, the number of Executions that will be deleted). This can be an estimate. |  [optional] |
|**purgeSample** | **List&lt;String&gt;** | A sample of the Execution names that will be deleted. Only populated if &#x60;force&#x60; is set to false. The maximum number of samples is 100 (it is possible to return fewer). |  [optional] |



