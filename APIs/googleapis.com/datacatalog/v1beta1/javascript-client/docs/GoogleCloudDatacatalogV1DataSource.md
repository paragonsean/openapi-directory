# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1DataSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **String** | Full name of a resource as defined by the service. For example: &#x60;//bigquery.googleapis.com/projects/{PROJECT_ID}/locations/{LOCATION}/datasets/{DATASET_ID}/tables/{TABLE_ID}&#x60; | [optional] 
**service** | **String** | Service that physically stores the data. | [optional] 
**sourceEntry** | **String** | Output only. Data Catalog entry name, if applicable. | [optional] [readonly] 
**storageProperties** | [**GoogleCloudDatacatalogV1StorageProperties**](GoogleCloudDatacatalogV1StorageProperties.md) |  | [optional] 



## Enum: ServiceEnum


* `SERVICE_UNSPECIFIED` (value: `"SERVICE_UNSPECIFIED"`)

* `CLOUD_STORAGE` (value: `"CLOUD_STORAGE"`)

* `BIGQUERY` (value: `"BIGQUERY"`)




