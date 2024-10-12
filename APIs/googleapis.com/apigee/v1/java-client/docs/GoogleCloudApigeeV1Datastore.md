

# GoogleCloudApigeeV1Datastore

The data store defines the connection to export data repository (Cloud Storage, BigQuery), including the credentials used to access the data repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Datastore create time, in milliseconds since the epoch of 1970-01-01T00:00:00Z |  [optional] [readonly] |
|**datastoreConfig** | [**GoogleCloudApigeeV1DatastoreConfig**](GoogleCloudApigeeV1DatastoreConfig.md) |  |  [optional] |
|**displayName** | **String** | Required. Display name in UI |  [optional] |
|**lastUpdateTime** | **String** | Output only. Datastore last update time, in milliseconds since the epoch of 1970-01-01T00:00:00Z |  [optional] [readonly] |
|**org** | **String** | Output only. Organization that the datastore belongs to |  [optional] [readonly] |
|**self** | **String** | Output only. Resource link of Datastore. Example: &#x60;/organizations/{org}/analytics/datastores/{uuid}&#x60; |  [optional] [readonly] |
|**targetType** | **String** | Destination storage type. Supported types &#x60;gcs&#x60; or &#x60;bigquery&#x60;. |  [optional] |



