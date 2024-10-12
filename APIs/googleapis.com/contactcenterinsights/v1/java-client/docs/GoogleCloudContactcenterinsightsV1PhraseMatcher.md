

# GoogleCloudContactcenterinsightsV1PhraseMatcher

The phrase matcher resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationUpdateTime** | **String** | Output only. The most recent time at which the activation status was updated. |  [optional] [readonly] |
|**active** | **Boolean** | Applies the phrase matcher only when it is active. |  [optional] |
|**displayName** | **String** | The human-readable name of the phrase matcher. |  [optional] |
|**name** | **String** | The resource name of the phrase matcher. Format: projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher} |  [optional] |
|**phraseMatchRuleGroups** | [**List&lt;GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup&gt;**](GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup.md) | A list of phase match rule groups that are included in this matcher. |  [optional] |
|**revisionCreateTime** | **String** | Output only. The timestamp of when the revision was created. It is also the create time when a new matcher is added. |  [optional] [readonly] |
|**revisionId** | **String** | Output only. Immutable. The revision ID of the phrase matcher. A new revision is committed whenever the matcher is changed, except when it is activated or deactivated. A server generated random ID will be used. Example: locations/global/phraseMatchers/my-first-matcher@1234567 |  [optional] [readonly] |
|**roleMatch** | [**RoleMatchEnum**](#RoleMatchEnum) | The role whose utterances the phrase matcher should be matched against. If the role is ROLE_UNSPECIFIED it will be matched against any utterances in the transcript. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of this phrase matcher. |  [optional] |
|**updateTime** | **String** | Output only. The most recent time at which the phrase matcher was updated. |  [optional] [readonly] |
|**versionTag** | **String** | The customized version tag to use for the phrase matcher. If not specified, it will default to &#x60;revision_id&#x60;. |  [optional] |



## Enum: RoleMatchEnum

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;ROLE_UNSPECIFIED&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |
| AUTOMATED_AGENT | &quot;AUTOMATED_AGENT&quot; |
| END_USER | &quot;END_USER&quot; |
| ANY_AGENT | &quot;ANY_AGENT&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PHRASE_MATCHER_TYPE_UNSPECIFIED | &quot;PHRASE_MATCHER_TYPE_UNSPECIFIED&quot; |
| ALL_OF | &quot;ALL_OF&quot; |
| ANY_OF | &quot;ANY_OF&quot; |



