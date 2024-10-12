

# GoogleCloudDatalabelingV1p1alpha1CreateInstructionMetadata

Metadata of a CreateInstruction operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Timestamp when create instruction request was created. |  [optional] |
|**instruction** | **String** | The name of the created Instruction. projects/{project_id}/instructions/{instruction_id} |  [optional] |
|**partialFailures** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | Partial failures encountered. E.g. single files that couldn&#39;t be read. Status details field will contain standard GCP error details. |  [optional] |



