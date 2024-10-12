

# Section

A section contains a collection of widgets that are rendered (vertically) in the order that they are specified. Across all platforms, cards have a narrow fixed width, so there's currently no need for layout properties (for example, float).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**header** | **String** | The header of the section. Formatted text is supported. For more information about formatting text, see [Formatting text in Google Chat apps](https://developers.google.com/chat/format-messages#card-formatting) and [Formatting text in Google Workspace Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting). |  [optional] |
|**widgets** | [**List&lt;WidgetMarkup&gt;**](WidgetMarkup.md) | A section must contain at least one widget. |  [optional] |



