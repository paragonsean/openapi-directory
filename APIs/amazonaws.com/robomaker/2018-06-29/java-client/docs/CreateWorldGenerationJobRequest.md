

# CreateWorldGenerationJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |  [optional] |
|**template** | **String** | The Amazon Resource Name (arn) of the world template describing the worlds you want to create. |  |
|**worldCount** | [**CreateWorldGenerationJobRequestWorldCount**](CreateWorldGenerationJobRequestWorldCount.md) |  |  |
|**tags** | **Map&lt;String, String&gt;** | A map that contains tag keys and tag values that are attached to the world generator job. |  [optional] |
|**worldTags** | **Map&lt;String, String&gt;** | A map that contains tag keys and tag values that are attached to the generated worlds. |  [optional] |



