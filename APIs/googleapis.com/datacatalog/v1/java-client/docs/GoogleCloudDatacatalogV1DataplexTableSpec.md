

# GoogleCloudDatacatalogV1DataplexTableSpec

Entry specification for a Dataplex table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataplexSpec** | [**GoogleCloudDatacatalogV1DataplexSpec**](GoogleCloudDatacatalogV1DataplexSpec.md) |  |  [optional] |
|**externalTables** | [**List&lt;GoogleCloudDatacatalogV1DataplexExternalTable&gt;**](GoogleCloudDatacatalogV1DataplexExternalTable.md) | List of external tables registered by Dataplex in other systems based on the same underlying data. External tables allow to query this data in those systems. |  [optional] |
|**userManaged** | **Boolean** | Indicates if the table schema is managed by the user or not. |  [optional] |



