# AmazonConnectService.StartOutboundVoiceContactRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationPhoneNumber** | **String** | The phone number of the customer, in E.164 format. | 
**contactFlowId** | **String** | &lt;p&gt;The identifier of the flow for the outbound call. To see the ContactFlowId in the Amazon Connect console user interface, on the navigation menu go to &lt;b&gt;Routing&lt;/b&gt;, &lt;b&gt;Contact Flows&lt;/b&gt;. Choose the flow. On the flow page, under the name of the flow, choose &lt;b&gt;Show additional flow information&lt;/b&gt;. The ContactFlowId is the last part of the ARN, shown here in bold: &lt;/p&gt; &lt;p&gt;arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/&lt;b&gt;846ec553-a005-41c0-8341-xxxxxxxxxxxx&lt;/b&gt; &lt;/p&gt; | 
**instanceId** | **String** | The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.  | [optional] 
**sourcePhoneNumber** | **String** | The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue. | [optional] 
**queueId** | **String** | The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the flow is used. If you do not specify a queue, you must specify a source phone number. | [optional] 
**attributes** | **{String: String}** | &lt;p&gt;A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in flows just like any other contact attributes.&lt;/p&gt; &lt;p&gt;There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.&lt;/p&gt; | [optional] 
**answerMachineDetectionConfig** | [**StartOutboundVoiceContactRequestAnswerMachineDetectionConfig**](StartOutboundVoiceContactRequestAnswerMachineDetectionConfig.md) |  | [optional] 
**campaignId** | **String** | The campaign identifier of the outbound communication. | [optional] 
**trafficType** | **String** | Denotes the class of traffic. Calls with different traffic types are handled differently by Amazon Connect. The default value is &lt;code&gt;GENERAL&lt;/code&gt;. Use &lt;code&gt;CAMPAIGN&lt;/code&gt; if &lt;code&gt;EnableAnswerMachineDetection&lt;/code&gt; is set to &lt;code&gt;true&lt;/code&gt;. For all other cases, use &lt;code&gt;GENERAL&lt;/code&gt;.  | [optional] 



## Enum: TrafficTypeEnum


* `GENERAL` (value: `"GENERAL"`)

* `CAMPAIGN` (value: `"CAMPAIGN"`)




