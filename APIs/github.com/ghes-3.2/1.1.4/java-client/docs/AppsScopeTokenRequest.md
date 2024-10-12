

# AppsScopeTokenRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | The OAuth access token used to authenticate to the GitHub API. |  |
|**permissions** | [**AppPermissions**](AppPermissions.md) |  |  [optional] |
|**repositories** | **List&lt;String&gt;** | The list of repository names to scope the user-to-server access token to. &#x60;repositories&#x60; may not be specified if &#x60;repository_ids&#x60; is specified. |  [optional] |
|**repositoryIds** | **List&lt;Integer&gt;** | The list of repository IDs to scope the user-to-server access token to. &#x60;repository_ids&#x60; may not be specified if &#x60;repositories&#x60; is specified. |  [optional] |
|**target** | **String** | The name of the user or organization to scope the user-to-server access token to. **Required** unless &#x60;target_id&#x60; is specified. |  [optional] |
|**targetId** | **Integer** | The ID of the user or organization to scope the user-to-server access token to. **Required** unless &#x60;target&#x60; is specified. |  [optional] |



