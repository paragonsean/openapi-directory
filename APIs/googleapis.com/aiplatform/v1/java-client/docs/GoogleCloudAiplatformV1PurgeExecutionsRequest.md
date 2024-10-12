

# GoogleCloudAiplatformV1PurgeExecutionsRequest

Request message for MetadataService.PurgeExecutions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | **String** | Required. A required filter matching the Executions to be purged. E.g., &#x60;update_time &lt;&#x3D; 2020-11-19T11:30:00-04:00&#x60;. |  [optional] |
|**force** | **Boolean** | Optional. Flag to indicate to actually perform the purge. If &#x60;force&#x60; is set to false, the method will return a sample of Execution names that would be deleted. |  [optional] |



