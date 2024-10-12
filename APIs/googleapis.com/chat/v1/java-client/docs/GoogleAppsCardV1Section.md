

# GoogleAppsCardV1Section

A section contains a collection of widgets that are rendered vertically in the order that they're specified. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collapsible** | **Boolean** | Indicates whether this section is collapsible. Collapsible sections hide some or all widgets, but users can expand the section to reveal the hidden widgets by clicking **Show more**. Users can hide the widgets again by clicking **Show less**. To determine which widgets are hidden, specify &#x60;uncollapsibleWidgetsCount&#x60;. |  [optional] |
|**header** | **String** | Text that appears at the top of a section. Supports simple HTML formatted text. For more information about formatting text, see [Formatting text in Google Chat apps](https://developers.google.com/chat/format-messages#card-formatting) and [Formatting text in Google Workspace Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting). |  [optional] |
|**uncollapsibleWidgetsCount** | **Integer** | The number of uncollapsible widgets which remain visible even when a section is collapsed. For example, when a section contains five widgets and the &#x60;uncollapsibleWidgetsCount&#x60; is set to &#x60;2&#x60;, the first two widgets are always shown and the last three are collapsed by default. The &#x60;uncollapsibleWidgetsCount&#x60; is taken into account only when &#x60;collapsible&#x60; is &#x60;true&#x60;. |  [optional] |
|**widgets** | [**List&lt;GoogleAppsCardV1Widget&gt;**](GoogleAppsCardV1Widget.md) | All the widgets in the section. Must contain at least one widget. |  [optional] |



