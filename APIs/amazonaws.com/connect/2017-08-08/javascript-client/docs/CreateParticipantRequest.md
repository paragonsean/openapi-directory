# AmazonConnectService.CreateParticipantRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceId** | **String** | The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.  | 
**contactId** | **String** | The identifier of the contact in this instance of Amazon Connect. Only contacts in the CHAT channel are supported. | 
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. | [optional] 
**participantDetails** | [**CreateParticipantRequestParticipantDetails**](CreateParticipantRequestParticipantDetails.md) |  | 


