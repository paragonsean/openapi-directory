# DataprocMetastoreApi.BackendMetastore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metastoreType** | **String** | The type of the backend metastore. | [optional] 
**name** | **String** | The relative resource name of the metastore that is being federated. The formats of the relative resource names for the currently supported metastores are listed below: BigQuery projects/{project_id} Dataproc Metastore projects/{project_id}/locations/{location}/services/{service_id} | [optional] 



## Enum: MetastoreTypeEnum


* `METASTORE_TYPE_UNSPECIFIED` (value: `"METASTORE_TYPE_UNSPECIFIED"`)

* `BIGQUERY` (value: `"BIGQUERY"`)

* `DATAPROC_METASTORE` (value: `"DATAPROC_METASTORE"`)




