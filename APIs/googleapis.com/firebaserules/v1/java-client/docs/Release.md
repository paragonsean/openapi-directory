

# Release

`Release` is a named reference to a `Ruleset`. Once a `Release` refers to a `Ruleset`, rules-enabled services will be able to enforce the `Ruleset`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time the release was created. |  [optional] [readonly] |
|**name** | **String** | Required. Format: &#x60;projects/{project_id}/releases/{release_id}&#x60; |  [optional] |
|**rulesetName** | **String** | Required. Name of the &#x60;Ruleset&#x60; referred to by this &#x60;Release&#x60;. The &#x60;Ruleset&#x60; must exist for the &#x60;Release&#x60; to be created. |  [optional] |
|**updateTime** | **String** | Output only. Time the release was updated. |  [optional] [readonly] |



