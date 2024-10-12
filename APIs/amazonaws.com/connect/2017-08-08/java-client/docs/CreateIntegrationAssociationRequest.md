

# CreateIntegrationAssociationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**integrationType** | [**IntegrationTypeEnum**](#IntegrationTypeEnum) | The type of information to be ingested. |  |
|**integrationArn** | **String** | &lt;p&gt;The Amazon Resource Name (ARN) of the integration.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When integrating with Amazon Pinpoint, the Amazon Connect and Amazon Pinpoint instances must be in the same account.&lt;/p&gt; &lt;/note&gt; |  |
|**sourceApplicationUrl** | **String** | The URL for the external application. This field is only required for the EVENT integration type. |  [optional] |
|**sourceApplicationName** | **String** | The name of the external application. This field is only required for the EVENT integration type. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | The type of the data source. This field is only required for the EVENT integration type. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |



## Enum: IntegrationTypeEnum

| Name | Value |
|---- | -----|
| EVENT | &quot;EVENT&quot; |
| VOICE_ID | &quot;VOICE_ID&quot; |
| PINPOINT_APP | &quot;PINPOINT_APP&quot; |
| WISDOM_ASSISTANT | &quot;WISDOM_ASSISTANT&quot; |
| WISDOM_KNOWLEDGE_BASE | &quot;WISDOM_KNOWLEDGE_BASE&quot; |
| CASES_DOMAIN | &quot;CASES_DOMAIN&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| SALESFORCE | &quot;SALESFORCE&quot; |
| ZENDESK | &quot;ZENDESK&quot; |



