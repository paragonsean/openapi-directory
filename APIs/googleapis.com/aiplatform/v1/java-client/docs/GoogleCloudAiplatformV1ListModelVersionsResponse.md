

# GoogleCloudAiplatformV1ListModelVersionsResponse

Response message for ModelService.ListModelVersions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**models** | [**List&lt;GoogleCloudAiplatformV1Model&gt;**](GoogleCloudAiplatformV1Model.md) | List of Model versions in the requested page. In the returned Model name field, version ID instead of regvision tag will be included. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass to ListModelVersionsRequest.page_token to obtain that page. |  [optional] |



