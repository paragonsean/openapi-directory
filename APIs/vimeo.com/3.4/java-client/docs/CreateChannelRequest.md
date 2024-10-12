

# CreateChannelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the channel. |  [optional] |
|**link** | **String** | The link to access the channel. You can use a custom name in the URL in place of a numeric channel ID, as in &#x60;/channels/{url_custom}&#x60;. |  [optional] |
|**name** | **String** | The name of the channel. |  |
|**privacy** | [**PrivacyEnum**](#PrivacyEnum) | The privacy level of the channel. |  |



## Enum: PrivacyEnum

| Name | Value |
|---- | -----|
| ANYBODY | &quot;anybody&quot; |
| MODERATORS | &quot;moderators&quot; |
| USER | &quot;user&quot; |



