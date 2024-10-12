

# GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatus

Resync status for each document per inconsistency type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentId** | [**GoogleCloudDocumentaiUiv1beta3DocumentId**](GoogleCloudDocumentaiUiv1beta3DocumentId.md) |  |  [optional] |
|**documentInconsistencyType** | [**DocumentInconsistencyTypeEnum**](#DocumentInconsistencyTypeEnum) | The type of document inconsistency. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |



## Enum: DocumentInconsistencyTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DOCUMENT_INCONSISTENCY_TYPE_UNSPECIFIED&quot; |
| INVALID_DOCPROTO | &quot;DOCUMENT_INCONSISTENCY_TYPE_INVALID_DOCPROTO&quot; |
| MISMATCHED_METADATA | &quot;DOCUMENT_INCONSISTENCY_TYPE_MISMATCHED_METADATA&quot; |
| NO_PAGE_IMAGE | &quot;DOCUMENT_INCONSISTENCY_TYPE_NO_PAGE_IMAGE&quot; |



