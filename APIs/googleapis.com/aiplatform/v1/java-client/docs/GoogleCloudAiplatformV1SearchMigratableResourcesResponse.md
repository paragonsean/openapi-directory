

# GoogleCloudAiplatformV1SearchMigratableResourcesResponse

Response message for MigrationService.SearchMigratableResources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**migratableResources** | [**List&lt;GoogleCloudAiplatformV1MigratableResource&gt;**](GoogleCloudAiplatformV1MigratableResource.md) | All migratable resources that can be migrated to the location specified in the request. |  [optional] |
|**nextPageToken** | **String** | The standard next-page token. The migratable_resources may not fill page_size in SearchMigratableResourcesRequest even when there are subsequent pages. |  [optional] |



