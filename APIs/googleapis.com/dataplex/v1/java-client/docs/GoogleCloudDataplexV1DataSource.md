

# GoogleCloudDataplexV1DataSource

The data source for DataScan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | **String** | Immutable. The Dataplex entity that represents the data source (e.g. BigQuery table) for DataScan, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}. |  [optional] |
|**resource** | **String** | Immutable. The service-qualified full resource name of the cloud resource for a DataScan job to scan against. The field could be: BigQuery table of type \&quot;TABLE\&quot; for DataProfileScan/DataQualityScan Format: //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID |  [optional] |



