# GitHubV3RestApi.MigrationsStartForOrgRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **[String]** | Exclude related items from being returned in the response in order to improve performance of the request. The array can include any of: &#x60;\&quot;repositories\&quot;&#x60;. | [optional] 
**excludeAttachments** | **Boolean** | Indicates whether attachments should be excluded from the migration (to reduce migration archive file size). | [optional] [default to false]
**excludeGitData** | **Boolean** | Indicates whether the repository git data should be excluded from the migration. | [optional] [default to false]
**excludeMetadata** | **Boolean** | Indicates whether metadata should be excluded and only git source should be included for the migration. | [optional] [default to false]
**excludeOwnerProjects** | **Boolean** | Indicates whether projects owned by the organization or users should be excluded. from the migration. | [optional] [default to false]
**excludeReleases** | **Boolean** | Indicates whether releases should be excluded from the migration (to reduce migration archive file size). | [optional] [default to false]
**lockRepositories** | **Boolean** | Indicates whether repositories should be locked (to prevent manipulation) while migrating data. | [optional] [default to false]
**orgMetadataOnly** | **Boolean** | Indicates whether this should only include organization metadata (repositories array should be empty and will ignore other flags). | [optional] [default to false]
**repositories** | **[String]** | A list of arrays indicating which repositories should be migrated. | 



## Enum: [ExcludeEnum]


* `repositories` (value: `"repositories"`)




