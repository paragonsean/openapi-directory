

# GoogleCloudAiplatformV1IndexDatapoint

A datapoint of Index.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crowdingTag** | [**GoogleCloudAiplatformV1IndexDatapointCrowdingTag**](GoogleCloudAiplatformV1IndexDatapointCrowdingTag.md) |  |  [optional] |
|**datapointId** | **String** | Required. Unique identifier of the datapoint. |  [optional] |
|**featureVector** | **List&lt;Float&gt;** | Required. Feature embedding vector. An array of numbers with the length of [NearestNeighborSearchConfig.dimensions]. |  [optional] |
|**numericRestricts** | [**List&lt;GoogleCloudAiplatformV1IndexDatapointNumericRestriction&gt;**](GoogleCloudAiplatformV1IndexDatapointNumericRestriction.md) | Optional. List of Restrict of the datapoint, used to perform \&quot;restricted searches\&quot; where boolean rule are used to filter the subset of the database eligible for matching. This uses numeric comparisons. |  [optional] |
|**restricts** | [**List&lt;GoogleCloudAiplatformV1IndexDatapointRestriction&gt;**](GoogleCloudAiplatformV1IndexDatapointRestriction.md) | Optional. List of Restrict of the datapoint, used to perform \&quot;restricted searches\&quot; where boolean rule are used to filter the subset of the database eligible for matching. This uses categorical tokens. See: https://cloud.google.com/vertex-ai/docs/matching-engine/filtering |  [optional] |



