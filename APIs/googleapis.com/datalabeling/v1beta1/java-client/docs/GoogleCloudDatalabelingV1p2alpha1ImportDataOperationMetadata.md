

# GoogleCloudDatalabelingV1p2alpha1ImportDataOperationMetadata

Metadata of an ImportData operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when import dataset request was created. |  [optional] |
|**dataset** | **String** | Output only. The name of imported dataset. \&quot;projects/_*_/datasets/_*\&quot; |  [optional] |
|**partialFailures** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | Output only. Partial failures encountered. E.g. single files that couldn&#39;t be read. Status details field will contain standard GCP error details. |  [optional] |



