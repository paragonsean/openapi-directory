

# ListMigrationJobsResponse

Response message for 'ListMigrationJobs' request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**migrationJobs** | [**List&lt;MigrationJob&gt;**](MigrationJob.md) | The list of migration jobs objects. |  [optional] |
|**nextPageToken** | **String** | A token which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



