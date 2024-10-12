

# GoogleCloudDatalabelingV1p2alpha1ExportDataOperationResponse

Response used for ExportDataset longrunning operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotatedDataset** | **String** | Output only. The name of annotated dataset in format \&quot;projects/_*_/datasets/_*_/annotatedDatasets/_*\&quot;. |  [optional] |
|**dataset** | **String** | Ouptut only. The name of dataset. \&quot;projects/_*_/datasets/_*\&quot; |  [optional] |
|**exportCount** | **Integer** | Output only. Number of examples exported successfully. |  [optional] |
|**labelStats** | [**GoogleCloudDatalabelingV1p2alpha1LabelStats**](GoogleCloudDatalabelingV1p2alpha1LabelStats.md) |  |  [optional] |
|**outputConfig** | [**GoogleCloudDatalabelingV1p2alpha1OutputConfig**](GoogleCloudDatalabelingV1p2alpha1OutputConfig.md) |  |  [optional] |
|**totalCount** | **Integer** | Output only. Total number of examples requested to export |  [optional] |



