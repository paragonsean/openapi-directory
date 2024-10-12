

# FromProperty


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Your ID for the platform that you are sending from.  **Messenger**: This value should be the &#x60;to.id&#x60; value you received in the inbound messenger event.  **Viber**: This is your Service Message ID given to you by your Vonage Account Manager. To find out more please visit [vonage.com](https://www.vonage.com/communications-apis/messages/).  **SMS**: **MMS**: or **WhatsApp** This value is not required.  |  [optional] |
|**number** | **String** | **SMS**: or **MMS**: The phone number of the message sender in the [E.164](https://en.wikipedia.org/wiki/E.164) format.  **WhatsApp**: This is your WhatsApp Business Number given to you by your Vonage Account Manager. To find out more please visit [vonage.com](https://www.vonage.com/communications-apis/messages/).  **Messenger**: or **Viber**: This value is not required.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of message that you want to send. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |
| VIBER_SERVICE_MSG | &quot;viber_service_msg&quot; |
| MESSENGER | &quot;messenger&quot; |
| WHATSAPP | &quot;whatsapp&quot; |



