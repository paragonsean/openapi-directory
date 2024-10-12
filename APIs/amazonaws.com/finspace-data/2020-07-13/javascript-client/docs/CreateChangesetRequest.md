# FinSpacePublicApi.CreateChangesetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | Idempotence Token for API operations | [optional] 
**changeType** | **String** | Indicates how the given change will be applied to the dataset. | 
**sourceParams** | **{String: String}** | Source Parameters of a Changeset | 
**formatParams** | **{String: String}** | Format Parameters of a Changeset | 



## Enum: ChangeTypeEnum


* `REPLACE` (value: `"REPLACE"`)

* `APPEND` (value: `"APPEND"`)

* `MODIFY` (value: `"MODIFY"`)




