

# CreateContactFlowRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the flow. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the flow. For descriptions of the available types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types\&quot;&gt;Choose a flow type&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. |  |
|**description** | **String** | The description of the flow.  |  [optional] |
|**content** | **String** | The content of the flow.  |  |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CONTACT_FLOW | &quot;CONTACT_FLOW&quot; |
| CUSTOMER_QUEUE | &quot;CUSTOMER_QUEUE&quot; |
| CUSTOMER_HOLD | &quot;CUSTOMER_HOLD&quot; |
| CUSTOMER_WHISPER | &quot;CUSTOMER_WHISPER&quot; |
| AGENT_HOLD | &quot;AGENT_HOLD&quot; |
| AGENT_WHISPER | &quot;AGENT_WHISPER&quot; |
| OUTBOUND_WHISPER | &quot;OUTBOUND_WHISPER&quot; |
| AGENT_TRANSFER | &quot;AGENT_TRANSFER&quot; |
| QUEUE_TRANSFER | &quot;QUEUE_TRANSFER&quot; |



