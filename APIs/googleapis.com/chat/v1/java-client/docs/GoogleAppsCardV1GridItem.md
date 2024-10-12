

# GoogleAppsCardV1GridItem

Represents an item in a grid layout. Items can contain text, an image, or both text and an image. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | A user-specified identifier for this grid item. This identifier is returned in the parent grid&#39;s &#x60;onClick&#x60; callback parameters. |  [optional] |
|**image** | [**GoogleAppsCardV1ImageComponent**](GoogleAppsCardV1ImageComponent.md) |  |  [optional] |
|**layout** | [**LayoutEnum**](#LayoutEnum) | The layout to use for the grid item. |  [optional] |
|**subtitle** | **String** | The grid item&#39;s subtitle. |  [optional] |
|**title** | **String** | The grid item&#39;s title. |  [optional] |



## Enum: LayoutEnum

| Name | Value |
|---- | -----|
| GRID_ITEM_LAYOUT_UNSPECIFIED | &quot;GRID_ITEM_LAYOUT_UNSPECIFIED&quot; |
| TEXT_BELOW | &quot;TEXT_BELOW&quot; |
| TEXT_ABOVE | &quot;TEXT_ABOVE&quot; |



