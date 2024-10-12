# ArtifactRegistryApi.CleanupPolicyCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newerThan** | **String** | Match versions newer than a duration. | [optional] 
**olderThan** | **String** | Match versions older than a duration. | [optional] 
**packageNamePrefixes** | **[String]** | Match versions by package prefix. Applied on any prefix match. | [optional] 
**tagPrefixes** | **[String]** | Match versions by tag prefix. Applied on any prefix match. | [optional] 
**tagState** | **String** | Match versions by tag status. | [optional] 
**versionNamePrefixes** | **[String]** | Match versions by version name prefix. Applied on any prefix match. | [optional] 



## Enum: TagStateEnum


* `TAG_STATE_UNSPECIFIED` (value: `"TAG_STATE_UNSPECIFIED"`)

* `TAGGED` (value: `"TAGGED"`)

* `UNTAGGED` (value: `"UNTAGGED"`)

* `ANY` (value: `"ANY"`)




