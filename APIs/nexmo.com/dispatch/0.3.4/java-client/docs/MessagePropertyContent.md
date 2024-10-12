

# MessagePropertyContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audio** | [**AudioProperty**](AudioProperty.md) |  |  [optional] |
|**_file** | [**FileProperty**](FileProperty.md) |  |  [optional] |
|**image** | [**ImageProperty**](ImageProperty.md) |  |  [optional] |
|**template** | [**TemplateProperty**](TemplateProperty.md) |  |  [optional] |
|**text** | **String** | The text of the message.  **Messenger**: Is limited to 640 characters  **SMS** or **Viber**: Is 1000 characters  **WhatsApp**: is 4096 characters  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of message that you are sending.  **Messenger**: supports &#x60;text&#x60;, &#x60;image&#x60;, &#x60;audio&#x60;, &#x60;video&#x60; and &#x60;file&#x60;.  **Viber Business Messages**: supports &#x60;image&#x60; and &#x60;text&#x60;.  **WhatsApp**: supports &#x60;template&#x60;, &#x60;text&#x60;, &#x60;image&#x60;, &#x60;audio&#x60;, &#x60;video&#x60; and &#x60;file&#x60;.  **SMS**: supports &#x60;text&#x60;.  |  |
|**video** | [**VideoProperty**](VideoProperty.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| IMAGE | &quot;image&quot; |
| AUDIO | &quot;audio&quot; |
| VIDEO | &quot;video&quot; |
| FILE | &quot;file&quot; |
| TEMPLATE | &quot;template&quot; |
| CUSTOM | &quot;custom&quot; |



