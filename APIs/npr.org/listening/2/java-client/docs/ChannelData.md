

# ChannelData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A longer description of what this channel focuses on |  |
|**displayType** | [**DisplayTypeEnum**](#DisplayTypeEnum) | How clients should display this channel in the explore view |  [optional] |
|**emptyText** | **String** | Text for clients to display when the channel contains no recommendations |  [optional] |
|**fullName** | **String** | A short description of what this channel focuses on |  |
|**id** | **String** | The actual value that should be sent |  |
|**refreshRule** | **Integer** | In the explore view of a client, this field indicates how this channel should be refreshed.  This is an experimental field and subject to change, but for now zero indicates the client should refresh this channel every time a START rating is sent for a type&#x3D;audio recommendation, while a 1 would indicate it can be refreshed much less often, such as on a 30 minute timer. 2 would indicate even less time to update, say every hour. We are still experimenting on the number of rules necessary and the best implementation for each type of rule.  |  [optional] |



## Enum: DisplayTypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| SHOW | &quot;show&quot; |
| PLAYABLE | &quot;playable&quot; |
| NEWSCAST | &quot;newscast&quot; |



