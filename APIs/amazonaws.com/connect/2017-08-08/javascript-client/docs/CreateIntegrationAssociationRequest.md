# AmazonConnectService.CreateIntegrationAssociationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrationType** | **String** | The type of information to be ingested. | 
**integrationArn** | **String** | &lt;p&gt;The Amazon Resource Name (ARN) of the integration.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When integrating with Amazon Pinpoint, the Amazon Connect and Amazon Pinpoint instances must be in the same account.&lt;/p&gt; &lt;/note&gt; | 
**sourceApplicationUrl** | **String** | The URL for the external application. This field is only required for the EVENT integration type. | [optional] 
**sourceApplicationName** | **String** | The name of the external application. This field is only required for the EVENT integration type. | [optional] 
**sourceType** | **String** | The type of the data source. This field is only required for the EVENT integration type. | [optional] 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. | [optional] 



## Enum: IntegrationTypeEnum


* `EVENT` (value: `"EVENT"`)

* `VOICE_ID` (value: `"VOICE_ID"`)

* `PINPOINT_APP` (value: `"PINPOINT_APP"`)

* `WISDOM_ASSISTANT` (value: `"WISDOM_ASSISTANT"`)

* `WISDOM_KNOWLEDGE_BASE` (value: `"WISDOM_KNOWLEDGE_BASE"`)

* `CASES_DOMAIN` (value: `"CASES_DOMAIN"`)





## Enum: SourceTypeEnum


* `SALESFORCE` (value: `"SALESFORCE"`)

* `ZENDESK` (value: `"ZENDESK"`)




