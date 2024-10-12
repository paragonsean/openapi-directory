# DatabaseMigrationApi.ListMigrationJobsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrationJobs** | [**[MigrationJob]**](MigrationJob.md) | The list of migration jobs objects. | [optional] 
**nextPageToken** | **String** | A token which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


