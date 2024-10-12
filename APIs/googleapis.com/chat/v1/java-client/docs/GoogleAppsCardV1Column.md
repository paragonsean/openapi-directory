

# GoogleAppsCardV1Column

A column. [Google Chat apps](https://developers.google.com/chat):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**horizontalAlignment** | [**HorizontalAlignmentEnum**](#HorizontalAlignmentEnum) | Specifies whether widgets align to the left, right, or center of a column. |  [optional] |
|**horizontalSizeStyle** | [**HorizontalSizeStyleEnum**](#HorizontalSizeStyleEnum) | Specifies how a column fills the width of the card. [Google Chat apps](https://developers.google.com/chat): |  [optional] |
|**verticalAlignment** | [**VerticalAlignmentEnum**](#VerticalAlignmentEnum) | Specifies whether widgets align to the top, bottom, or center of a column. [Google Chat apps](https://developers.google.com/chat): |  [optional] |
|**widgets** | [**List&lt;GoogleAppsCardV1Widgets&gt;**](GoogleAppsCardV1Widgets.md) | An array of widgets included in a column. Widgets appear in the order that they are specified. |  [optional] |



## Enum: HorizontalAlignmentEnum

| Name | Value |
|---- | -----|
| HORIZONTAL_ALIGNMENT_UNSPECIFIED | &quot;HORIZONTAL_ALIGNMENT_UNSPECIFIED&quot; |
| START | &quot;START&quot; |
| CENTER | &quot;CENTER&quot; |
| END | &quot;END&quot; |



## Enum: HorizontalSizeStyleEnum

| Name | Value |
|---- | -----|
| HORIZONTAL_SIZE_STYLE_UNSPECIFIED | &quot;HORIZONTAL_SIZE_STYLE_UNSPECIFIED&quot; |
| FILL_AVAILABLE_SPACE | &quot;FILL_AVAILABLE_SPACE&quot; |
| FILL_MINIMUM_SPACE | &quot;FILL_MINIMUM_SPACE&quot; |



## Enum: VerticalAlignmentEnum

| Name | Value |
|---- | -----|
| VERTICAL_ALIGNMENT_UNSPECIFIED | &quot;VERTICAL_ALIGNMENT_UNSPECIFIED&quot; |
| CENTER | &quot;CENTER&quot; |
| TOP | &quot;TOP&quot; |
| BOTTOM | &quot;BOTTOM&quot; |



