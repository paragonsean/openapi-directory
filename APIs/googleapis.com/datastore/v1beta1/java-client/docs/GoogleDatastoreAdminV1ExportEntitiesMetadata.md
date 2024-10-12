

# GoogleDatastoreAdminV1ExportEntitiesMetadata

Metadata for ExportEntities operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**common** | [**GoogleDatastoreAdminV1CommonMetadata**](GoogleDatastoreAdminV1CommonMetadata.md) |  |  [optional] |
|**entityFilter** | [**GoogleDatastoreAdminV1EntityFilter**](GoogleDatastoreAdminV1EntityFilter.md) |  |  [optional] |
|**outputUrlPrefix** | **String** | Location for the export metadata and data files. This will be the same value as the google.datastore.admin.v1.ExportEntitiesRequest.output_url_prefix field. The final output location is provided in google.datastore.admin.v1.ExportEntitiesResponse.output_url. |  [optional] |
|**progressBytes** | [**GoogleDatastoreAdminV1Progress**](GoogleDatastoreAdminV1Progress.md) |  |  [optional] |
|**progressEntities** | [**GoogleDatastoreAdminV1Progress**](GoogleDatastoreAdminV1Progress.md) |  |  [optional] |



