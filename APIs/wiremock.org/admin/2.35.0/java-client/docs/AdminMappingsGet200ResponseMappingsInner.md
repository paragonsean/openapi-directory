

# AdminMappingsGet200ResponseMappingsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | This stub mapping&#39;s unique identifier |  [optional] |
|**metadata** | **Object** | Arbitrary metadata to be used for e.g. tagging, documentation. Can also be used to find and remove stubs. |  [optional] |
|**name** | **String** | The stub mapping&#39;s name |  [optional] |
|**newScenarioState** | **String** | The new state for the scenario to be updated to after this stub is served. |  [optional] |
|**persistent** | **Boolean** | Indicates that the stub mapping should be persisted immediately on create/update/delete and survive resets to default. |  [optional] |
|**postServeActions** | **Object** | A map of the names of post serve action extensions to trigger and their parameters. |  [optional] |
|**priority** | **Integer** | This stub mapping&#39;s priority relative to others. 1 is highest. |  [optional] |
|**request** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md) |  |  [optional] |
|**requiredScenarioState** | **String** | The required state of the scenario in order for this stub to be matched. |  [optional] |
|**response** | [**AdminMappingsGet200ResponseMappingsInnerResponse**](AdminMappingsGet200ResponseMappingsInnerResponse.md) |  |  [optional] |
|**scenarioName** | **String** | The name of the scenario that this stub mapping is part of |  [optional] |
|**uuid** | **String** | Alias for the id |  [optional] |



