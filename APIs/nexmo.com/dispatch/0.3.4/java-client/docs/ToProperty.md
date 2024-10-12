

# ToProperty


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The ID of the message recipient.  **Messenger**: This value should be the &#x60;from.id&#x60; value you received in the inbound messenger event.  **SMS**: or **Viber**: or **WhatsApp** This value is not required.  |  [optional] |
|**number** | **String** | **SMS**: or **MMS**: or **Viber**: or **WhatsApp** The phone number of the message recipient in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Don&#39;t use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.  **Messenger**: This value is not required.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of message that you want to send. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |
| VIBER_SERVICE_MSG | &quot;viber_service_msg&quot; |
| MESSENGER | &quot;messenger&quot; |
| WHATSAPP | &quot;whatsapp&quot; |



