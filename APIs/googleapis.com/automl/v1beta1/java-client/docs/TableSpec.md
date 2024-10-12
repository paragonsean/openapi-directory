

# TableSpec

A specification of a relational table. The table's schema is represented via its child column specs. It is pre-populated as part of ImportData by schema inference algorithm, the version of which is a required parameter of ImportData InputConfig. Note: While working with a table, at times the schema may be inconsistent with the data in the table (e.g. string in a FLOAT64 column). The consistency validation is done upon creation of a model. Used by: * Tables

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnCount** | **String** | Output only. The number of columns of the table. That is, the number of child ColumnSpec-s. |  [optional] |
|**etag** | **String** | Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**inputConfigs** | [**List&lt;InputConfig&gt;**](InputConfig.md) | Output only. Input configs via which data currently residing in the table had been imported. |  [optional] |
|**name** | **String** | Output only. The resource name of the table spec. Form: &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/tableSpecs/{table_spec_id}&#x60; |  [optional] |
|**rowCount** | **String** | Output only. The number of rows (i.e. examples) in the table. |  [optional] |
|**timeColumnSpecId** | **String** | column_spec_id of the time column. Only used if the parent dataset&#39;s ml_use_column_spec_id is not set. Used to split rows into TRAIN, VALIDATE and TEST sets such that oldest rows go to TRAIN set, newest to TEST, and those in between to VALIDATE. Required type: TIMESTAMP. If both this column and ml_use_column are not set, then ML use of all rows will be assigned by AutoML. NOTE: Updates of this field will instantly affect any other users concurrently working with the dataset. |  [optional] |
|**validRowCount** | **String** | Output only. The number of valid rows (i.e. without values that don&#39;t match DataType-s of their columns). |  [optional] |



