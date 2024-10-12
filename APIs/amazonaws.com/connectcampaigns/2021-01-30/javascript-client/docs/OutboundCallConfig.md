# AmazonConnectCampaignService.OutboundCallConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answerMachineDetectionConfig** | [**AnswerMachineDetectionConfig**](AnswerMachineDetectionConfig.md) |  | [optional] 
**connectContactFlowId** | **String** | The identifier of the contact flow for the outbound call. | 
**connectQueueId** | **String** | The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the contact flow is used. If you do not specify a queue, you must specify a source phone number. | 
**connectSourcePhoneNumber** | **String** | The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue. | [optional] 


