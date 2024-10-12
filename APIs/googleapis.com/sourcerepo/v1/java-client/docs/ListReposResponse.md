

# ListReposResponse

Response for ListRepos. The size is not set in the returned repositories.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If non-empty, additional repositories exist within the project. These can be retrieved by including this value in the next ListReposRequest&#39;s page_token field. |  [optional] |
|**repos** | [**List&lt;Repo&gt;**](Repo.md) | The listed repos. |  [optional] |



