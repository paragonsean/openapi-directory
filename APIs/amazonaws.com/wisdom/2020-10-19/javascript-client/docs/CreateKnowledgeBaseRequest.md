# AmazonConnectWisdomService.CreateKnowledgeBaseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. | [optional] 
**description** | **String** | The description. | [optional] 
**knowledgeBaseType** | **String** | The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.  | 
**name** | **String** | The name of the knowledge base. | 
**renderingConfiguration** | [**CreateKnowledgeBaseRequestRenderingConfiguration**](CreateKnowledgeBaseRequestRenderingConfiguration.md) |  | [optional] 
**serverSideEncryptionConfiguration** | [**CreateAssistantRequestServerSideEncryptionConfiguration**](CreateAssistantRequestServerSideEncryptionConfiguration.md) |  | [optional] 
**sourceConfiguration** | [**CreateKnowledgeBaseRequestSourceConfiguration**](CreateKnowledgeBaseRequestSourceConfiguration.md) |  | [optional] 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. | [optional] 



## Enum: KnowledgeBaseTypeEnum


* `EXTERNAL` (value: `"EXTERNAL"`)

* `CUSTOM` (value: `"CUSTOM"`)




