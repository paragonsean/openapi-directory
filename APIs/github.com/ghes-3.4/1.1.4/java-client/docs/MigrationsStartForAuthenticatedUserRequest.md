

# MigrationsStartForAuthenticatedUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exclude** | [**List&lt;ExcludeEnum&gt;**](#List&lt;ExcludeEnum&gt;) | Exclude attributes from the API response to improve performance |  [optional] |
|**excludeAttachments** | **Boolean** | Do not include attachments in the migration |  [optional] |
|**excludeGitData** | **Boolean** | Indicates whether the repository git data should be excluded from the migration. |  [optional] |
|**excludeMetadata** | **Boolean** | Indicates whether metadata should be excluded and only git source should be included for the migration. |  [optional] |
|**excludeOwnerProjects** | **Boolean** | Indicates whether projects owned by the organization or users should be excluded. |  [optional] |
|**excludeReleases** | **Boolean** | Do not include releases in the migration |  [optional] |
|**lockRepositories** | **Boolean** | Lock the repositories being migrated at the start of the migration |  [optional] |
|**orgMetadataOnly** | **Boolean** | Indicates whether this should only include organization metadata (repositories array should be empty and will ignore other flags). |  [optional] |
|**repositories** | **List&lt;String&gt;** |  |  |



## Enum: List&lt;ExcludeEnum&gt;

| Name | Value |
|---- | -----|
| REPOSITORIES | &quot;repositories&quot; |



