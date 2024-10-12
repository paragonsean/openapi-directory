

# GoogleAppsCardV1OpenLink

Represents an `onClick` event that opens a hyperlink. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**onClose** | [**OnCloseEnum**](#OnCloseEnum) | Whether the client forgets about a link after opening it, or observes it until the window closes. [Google Workspace Add-ons](https://developers.google.com/workspace/add-ons): |  [optional] |
|**openAs** | [**OpenAsEnum**](#OpenAsEnum) | How to open a link. [Google Workspace Add-ons](https://developers.google.com/workspace/add-ons): |  [optional] |
|**url** | **String** | The URL to open. |  [optional] |



## Enum: OnCloseEnum

| Name | Value |
|---- | -----|
| NOTHING | &quot;NOTHING&quot; |
| RELOAD | &quot;RELOAD&quot; |



## Enum: OpenAsEnum

| Name | Value |
|---- | -----|
| FULL_SIZE | &quot;FULL_SIZE&quot; |
| OVERLAY | &quot;OVERLAY&quot; |



