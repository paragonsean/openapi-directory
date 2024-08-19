

# GoogleCloudAiplatformV1beta1MergeVersionAliasesRequest

Request message for ModelService.MergeVersionAliases.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**versionAliases** | **List&lt;String&gt;** | Required. The set of version aliases to merge. The alias should be at most 128 characters, and match &#x60;a-z{0,126}[a-z-0-9]&#x60;. Add the &#x60;-&#x60; prefix to an alias means removing that alias from the version. &#x60;-&#x60; is NOT counted in the 128 characters. Example: &#x60;-golden&#x60; means removing the &#x60;golden&#x60; alias from the version. There is NO ordering in aliases, which means 1) The aliases returned from GetModel API might not have the exactly same order from this MergeVersionAliases API. 2) Adding and deleting the same alias in the request is not recommended, and the 2 operations will be cancelled out. |  [optional] |



