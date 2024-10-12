

# MigrationsStartForOrgRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exclude** | [**List&lt;ExcludeEnum&gt;**](#List&lt;ExcludeEnum&gt;) | Exclude related items from being returned in the response in order to improve performance of the request. The array can include any of: &#x60;\&quot;repositories\&quot;&#x60;. |  [optional] |
|**excludeAttachments** | **Boolean** | Indicates whether attachments should be excluded from the migration (to reduce migration archive file size). |  [optional] |
|**excludeGitData** | **Boolean** | Indicates whether the repository git data should be excluded from the migration. |  [optional] |
|**excludeMetadata** | **Boolean** | Indicates whether metadata should be excluded and only git source should be included for the migration. |  [optional] |
|**excludeOwnerProjects** | **Boolean** | Indicates whether projects owned by the organization or users should be excluded. from the migration. |  [optional] |
|**excludeReleases** | **Boolean** | Indicates whether releases should be excluded from the migration (to reduce migration archive file size). |  [optional] |
|**lockRepositories** | **Boolean** | Indicates whether repositories should be locked (to prevent manipulation) while migrating data. |  [optional] |
|**orgMetadataOnly** | **Boolean** | Indicates whether this should only include organization metadata (repositories array should be empty and will ignore other flags). |  [optional] |
|**repositories** | **List&lt;String&gt;** | A list of arrays indicating which repositories should be migrated. |  |



## Enum: List&lt;ExcludeEnum&gt;

| Name | Value |
|---- | -----|
| REPOSITORIES | &quot;repositories&quot; |



