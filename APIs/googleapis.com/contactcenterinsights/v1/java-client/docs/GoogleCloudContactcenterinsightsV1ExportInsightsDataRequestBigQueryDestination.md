

# GoogleCloudContactcenterinsightsV1ExportInsightsDataRequestBigQueryDestination

A BigQuery Table Reference.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataset** | **String** | Required. The name of the BigQuery dataset that the snapshot result should be exported to. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error. |  [optional] |
|**projectId** | **String** | A project ID or number. If specified, then export will attempt to write data to this project instead of the resource project. Otherwise, the resource project will be used. |  [optional] |
|**table** | **String** | The BigQuery table name to which the insights data should be written. If this table does not exist, the export call returns an INVALID_ARGUMENT error. |  [optional] |



