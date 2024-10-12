# SmsApi.Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountRef** | **String** | **Advanced**: An optional string used to identify separate accounts using the SMS endpoint for billing purposes. To use this feature, please email [support@nexmo.com](mailto:support@nexmo.com) | [optional] 
**clientRef** | **String** | If a &#x60;client-ref&#x60; was included when sending the SMS, this field will be included and hold the value that was sent. | [optional] 
**messageId** | **String** | The ID of the message | [optional] 
**messagePrice** | **String** | The estimated cost of the message | [optional] 
**network** | **String** | The estimated ID of the network of the recipient | [optional] 
**remainingBalance** | **String** | Your estimated remaining balance | [optional] 
**status** | **String** | The status of the message. See [Troubleshooting Failed SMS](/messaging/sms/guides/troubleshooting-sms). | [optional] 
**to** | **String** | The number the message was sent to. Numbers are specified in E.164 format. | [optional] 


