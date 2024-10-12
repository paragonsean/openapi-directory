

# GoogleCloudDocumentaiV1beta2DocumentProvenance

Structure to identify provenance relationships between annotations in different revisions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | The Id of this operation. Needs to be unique within the scope of the revision. |  [optional] |
|**parents** | [**List&lt;GoogleCloudDocumentaiV1beta2DocumentProvenanceParent&gt;**](GoogleCloudDocumentaiV1beta2DocumentProvenanceParent.md) | References to the original elements that are replaced. |  [optional] |
|**revision** | **Integer** | The index of the revision that produced this element. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of provenance operation. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OPERATION_TYPE_UNSPECIFIED | &quot;OPERATION_TYPE_UNSPECIFIED&quot; |
| ADD | &quot;ADD&quot; |
| REMOVE | &quot;REMOVE&quot; |
| UPDATE | &quot;UPDATE&quot; |
| REPLACE | &quot;REPLACE&quot; |
| EVAL_REQUESTED | &quot;EVAL_REQUESTED&quot; |
| EVAL_APPROVED | &quot;EVAL_APPROVED&quot; |
| EVAL_SKIPPED | &quot;EVAL_SKIPPED&quot; |



