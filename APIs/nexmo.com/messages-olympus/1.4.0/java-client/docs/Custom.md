

# Custom


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. |  [optional] |
|**custom** | **Map&lt;String, Object&gt;** | A custom payload, which is passed directly to WhatsApp for certain features such as templates and interactive messages. The schema of a custom object can vary widely. [Read more about Custom Objects](https://developer.vonage.com/messages/concepts/custom-objects). |  [optional] |
|**messageType** | [**MessageTypeEnum**](#MessageTypeEnum) | The type of message to send. You must provide &#x60;custom&#x60; in this field |  |



## Enum: MessageTypeEnum

| Name | Value |
|---- | -----|
| CUSTOM | &quot;custom&quot; |



