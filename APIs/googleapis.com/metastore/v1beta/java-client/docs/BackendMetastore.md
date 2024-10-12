

# BackendMetastore

Represents a backend metastore for the federation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metastoreType** | [**MetastoreTypeEnum**](#MetastoreTypeEnum) | The type of the backend metastore. |  [optional] |
|**name** | **String** | The relative resource name of the metastore that is being federated. The formats of the relative resource names for the currently supported metastores are listed below: BigQuery projects/{project_id} Dataproc Metastore projects/{project_id}/locations/{location}/services/{service_id} |  [optional] |



## Enum: MetastoreTypeEnum

| Name | Value |
|---- | -----|
| METASTORE_TYPE_UNSPECIFIED | &quot;METASTORE_TYPE_UNSPECIFIED&quot; |
| DATAPLEX | &quot;DATAPLEX&quot; |
| BIGQUERY | &quot;BIGQUERY&quot; |
| DATAPROC_METASTORE | &quot;DATAPROC_METASTORE&quot; |



