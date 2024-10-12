

# AnalysisArchiveTransitionRule

A rule for auto-archiving image analysis by time and/or tag-history

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisAgeDays** | **Integer** | Matches if the analysis is strictly older than this number of days |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**exclude** | [**AnalysisArchiveTransitionRuleExclude**](AnalysisArchiveTransitionRuleExclude.md) |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**maxImagesPerAccount** | **Integer** | This is the maximum number of image analyses an account can have. Can only be set on system_global rules |  [optional] |
|**ruleId** | **String** | Unique identifier for archive rule |  [optional] |
|**selector** | [**ImageSelector**](ImageSelector.md) |  |  [optional] |
|**systemGlobal** | **Boolean** | True if the rule applies to all accounts in the system. This is only available to admin users to update/modify, but all users with permission to list rules can see them |  [optional] |
|**tagVersionsNewer** | **Integer** | Number of images mapped to the tag that are newer |  [optional] |
|**transition** | [**TransitionEnum**](#TransitionEnum) | The type of transition to make. If \&quot;archive\&quot;, then archive an image from the working set and remove it from the working set. If \&quot;delete\&quot;, then match against archived images and delete from the archive if match. |  |



## Enum: TransitionEnum

| Name | Value |
|---- | -----|
| ARCHIVE | &quot;archive&quot; |
| DELETE | &quot;delete&quot; |



