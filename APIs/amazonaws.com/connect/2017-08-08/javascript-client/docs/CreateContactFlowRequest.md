# AmazonConnectService.CreateContactFlowRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the flow. | 
**type** | **String** | The type of the flow. For descriptions of the available types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types\&quot;&gt;Choose a flow type&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. | 
**description** | **String** | The description of the flow.  | [optional] 
**content** | **String** | The content of the flow.  | 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. | [optional] 



## Enum: TypeEnum


* `CONTACT_FLOW` (value: `"CONTACT_FLOW"`)

* `CUSTOMER_QUEUE` (value: `"CUSTOMER_QUEUE"`)

* `CUSTOMER_HOLD` (value: `"CUSTOMER_HOLD"`)

* `CUSTOMER_WHISPER` (value: `"CUSTOMER_WHISPER"`)

* `AGENT_HOLD` (value: `"AGENT_HOLD"`)

* `AGENT_WHISPER` (value: `"AGENT_WHISPER"`)

* `OUTBOUND_WHISPER` (value: `"OUTBOUND_WHISPER"`)

* `AGENT_TRANSFER` (value: `"AGENT_TRANSFER"`)

* `QUEUE_TRANSFER` (value: `"QUEUE_TRANSFER"`)




