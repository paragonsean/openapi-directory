

# GoogleCloudDataplexV1DataProfileResultProfileField

A field within a table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | **String** | The mode of the field. Possible values include: REQUIRED, if it is a required field. NULLABLE, if it is an optional field. REPEATED, if it is a repeated field. |  [optional] |
|**name** | **String** | The name of the field. |  [optional] |
|**profile** | [**GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfo**](GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfo.md) |  |  [optional] |
|**type** | **String** | The data type retrieved from the schema of the data source. For instance, for a BigQuery native table, it is the BigQuery Table Schema (https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#tablefieldschema). For a Dataplex Entity, it is the Entity Schema (https://cloud.google.com/dataplex/docs/reference/rpc/google.cloud.dataplex.v1#type_3). |  [optional] |



