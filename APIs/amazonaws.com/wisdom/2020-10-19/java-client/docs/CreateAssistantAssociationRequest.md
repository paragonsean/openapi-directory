

# CreateAssistantAssociationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**association** | [**CreateAssistantAssociationRequestAssociation**](CreateAssistantAssociationRequestAssociation.md) |  |  |
|**associationType** | [**AssociationTypeEnum**](#AssociationTypeEnum) | The type of association. |  |
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. |  [optional] |



## Enum: AssociationTypeEnum

| Name | Value |
|---- | -----|
| KNOWLEDGE_BASE | &quot;KNOWLEDGE_BASE&quot; |



