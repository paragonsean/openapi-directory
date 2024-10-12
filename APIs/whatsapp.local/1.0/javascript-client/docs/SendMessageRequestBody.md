# WhatsAppBusinessApi.SendMessageRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | [**Audio**](Audio.md) |  | [optional] 
**contacts** | [**[Contact]**](Contact.md) |  | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**hsm** | [**Hsm**](Hsm.md) |  | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**previewUrl** | **Boolean** | Specifying preview_url in the request is optional when not including a URL in your message. To include a URL preview, set preview_url to true in the message body and make sure the URL begins with http:// or https://. For more information, see the Sending URLs in Text Messages section. | [optional] 
**recipientType** | **String** | Determines whether the recipient is an individual or a group Specifying recipient_type in the request is optional when the value is individual. However, recipient_type is required when using group. If sending a text message to a group, see the Sending Group Messages documentation. | [optional] [default to &#39;individual&#39;]
**text** | [**Text**](Text.md) |  | [optional] 
**to** | **String** | When recipient_type is individual, this field is the WhatsApp ID (phone number) returned from contacts endpoint. When recipient_type is group, this field is the WhatsApp group ID. | 
**ttl** | **Object** |  | [optional] 
**type** | [**MessageType**](MessageType.md) |  | [optional] 
**video** | [**Video**](Video.md) |  | [optional] 



## Enum: RecipientTypeEnum


* `individual` (value: `"individual"`)

* `group` (value: `"group"`)




