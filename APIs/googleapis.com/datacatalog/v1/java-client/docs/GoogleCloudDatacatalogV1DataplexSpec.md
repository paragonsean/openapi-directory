

# GoogleCloudDatacatalogV1DataplexSpec

Common Dataplex fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asset** | **String** | Fully qualified resource name of an asset in Dataplex, to which the underlying data source (Cloud Storage bucket or BigQuery dataset) of the entity is attached. |  [optional] |
|**compressionFormat** | **String** | Compression format of the data, e.g., zip, gzip etc. |  [optional] |
|**dataFormat** | [**GoogleCloudDatacatalogV1PhysicalSchema**](GoogleCloudDatacatalogV1PhysicalSchema.md) |  |  [optional] |
|**projectId** | **String** | Project ID of the underlying Cloud Storage or BigQuery data. Note that this may not be the same project as the correspondingly Dataplex lake / zone / asset. |  [optional] |



