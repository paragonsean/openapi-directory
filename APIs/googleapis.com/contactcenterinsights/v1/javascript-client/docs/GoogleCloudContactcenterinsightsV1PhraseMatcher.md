# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1PhraseMatcher

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationUpdateTime** | **String** | Output only. The most recent time at which the activation status was updated. | [optional] [readonly] 
**active** | **Boolean** | Applies the phrase matcher only when it is active. | [optional] 
**displayName** | **String** | The human-readable name of the phrase matcher. | [optional] 
**name** | **String** | The resource name of the phrase matcher. Format: projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher} | [optional] 
**phraseMatchRuleGroups** | [**[GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup]**](GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup.md) | A list of phase match rule groups that are included in this matcher. | [optional] 
**revisionCreateTime** | **String** | Output only. The timestamp of when the revision was created. It is also the create time when a new matcher is added. | [optional] [readonly] 
**revisionId** | **String** | Output only. Immutable. The revision ID of the phrase matcher. A new revision is committed whenever the matcher is changed, except when it is activated or deactivated. A server generated random ID will be used. Example: locations/global/phraseMatchers/my-first-matcher@1234567 | [optional] [readonly] 
**roleMatch** | **String** | The role whose utterances the phrase matcher should be matched against. If the role is ROLE_UNSPECIFIED it will be matched against any utterances in the transcript. | [optional] 
**type** | **String** | Required. The type of this phrase matcher. | [optional] 
**updateTime** | **String** | Output only. The most recent time at which the phrase matcher was updated. | [optional] [readonly] 
**versionTag** | **String** | The customized version tag to use for the phrase matcher. If not specified, it will default to &#x60;revision_id&#x60;. | [optional] 



## Enum: RoleMatchEnum


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `HUMAN_AGENT` (value: `"HUMAN_AGENT"`)

* `AUTOMATED_AGENT` (value: `"AUTOMATED_AGENT"`)

* `END_USER` (value: `"END_USER"`)

* `ANY_AGENT` (value: `"ANY_AGENT"`)





## Enum: TypeEnum


* `PHRASE_MATCHER_TYPE_UNSPECIFIED` (value: `"PHRASE_MATCHER_TYPE_UNSPECIFIED"`)

* `ALL_OF` (value: `"ALL_OF"`)

* `ANY_OF` (value: `"ANY_OF"`)




