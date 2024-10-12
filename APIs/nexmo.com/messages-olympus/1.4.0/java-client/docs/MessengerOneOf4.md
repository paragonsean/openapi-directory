

# MessengerOneOf4


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. |  [optional] |
|**_file** | [**MessengerOneOf4AllOfFile**](MessengerOneOf4AllOfFile.md) |  |  |
|**messageType** | [**MessageTypeEnum**](#MessageTypeEnum) | The type of message to send. You must provide &#x60;file&#x60; in this field |  |
|**channel** | [**ChannelEnum**](#ChannelEnum) | The channel to send to. You must provide &#x60;messenger&#x60; in this field |  |
|**from** | **String** | The ID of the message sender  |  |
|**messenger** | [**ChannelOptionsMessengerMessenger**](ChannelOptionsMessengerMessenger.md) |  |  [optional] |
|**to** | **String** | The ID of the message recipient  |  |



## Enum: MessageTypeEnum

| Name | Value |
|---- | -----|
| FILE | &quot;file&quot; |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| MESSENGER | &quot;messenger&quot; |



