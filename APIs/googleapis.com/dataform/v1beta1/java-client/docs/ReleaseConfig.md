

# ReleaseConfig

Represents a Dataform release configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codeCompilationConfig** | [**CodeCompilationConfig**](CodeCompilationConfig.md) |  |  [optional] |
|**cronSchedule** | **String** | Optional. Optional schedule (in cron format) for automatic creation of compilation results. |  [optional] |
|**disabled** | **Boolean** | Optional. Disables automatic creation of compilation results. |  [optional] |
|**gitCommitish** | **String** | Required. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: &#x60;12ade345&#x60; - a tag: &#x60;tag1&#x60; - a branch name: &#x60;branch1&#x60; |  [optional] |
|**name** | **String** | Output only. The release config&#39;s name. |  [optional] [readonly] |
|**recentScheduledReleaseRecords** | [**List&lt;ScheduledReleaseRecord&gt;**](ScheduledReleaseRecord.md) | Output only. Records of the 10 most recent scheduled release attempts, ordered in in descending order of &#x60;release_time&#x60;. Updated whenever automatic creation of a compilation result is triggered by cron_schedule. |  [optional] [readonly] |
|**releaseCompilationResult** | **String** | Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is automatically created from this release config (using cron_schedule), or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format &#x60;projects/_*_/locations/_*_/repositories/_*_/compilationResults/_*&#x60;. |  [optional] |
|**timeZone** | **String** | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC. |  [optional] |



