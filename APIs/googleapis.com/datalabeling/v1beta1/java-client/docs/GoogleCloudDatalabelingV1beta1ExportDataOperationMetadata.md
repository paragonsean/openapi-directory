

# GoogleCloudDatalabelingV1beta1ExportDataOperationMetadata

Metadata of an ExportData operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotatedDataset** | **String** | Output only. The name of annotated dataset in format \&quot;projects/_*_/datasets/_*_/annotatedDatasets/_*\&quot;. |  [optional] |
|**createTime** | **String** | Output only. Timestamp when export dataset request was created. |  [optional] |
|**dataset** | **String** | Output only. The name of dataset to be exported. \&quot;projects/_*_/datasets/_*\&quot; |  [optional] |
|**partialFailures** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | Output only. Partial failures encountered. E.g. single files that couldn&#39;t be read. Status details field will contain standard GCP error details. |  [optional] |



