

# GoogleAppsCardV1DecoratedText

A widget that displays text with optional decorations such as a label above or below the text, an icon in front of the text, a selection widget, or a button after the text. For an example in Google Chat apps, see [Decorated text](https://developers.google.com/chat/ui/widgets/decorated-text). [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bottomLabel** | **String** | The text that appears below &#x60;text&#x60;. Always wraps. |  [optional] |
|**button** | [**GoogleAppsCardV1Button**](GoogleAppsCardV1Button.md) |  |  [optional] |
|**endIcon** | [**GoogleAppsCardV1Icon**](GoogleAppsCardV1Icon.md) |  |  [optional] |
|**icon** | [**GoogleAppsCardV1Icon**](GoogleAppsCardV1Icon.md) |  |  [optional] |
|**onClick** | [**GoogleAppsCardV1OnClick**](GoogleAppsCardV1OnClick.md) |  |  [optional] |
|**startIcon** | [**GoogleAppsCardV1Icon**](GoogleAppsCardV1Icon.md) |  |  [optional] |
|**switchControl** | [**GoogleAppsCardV1SwitchControl**](GoogleAppsCardV1SwitchControl.md) |  |  [optional] |
|**text** | **String** | Required. The primary text. Supports simple formatting. For more information about formatting text, see [Formatting text in Google Chat apps](https://developers.google.com/chat/format-messages#card-formatting) and [Formatting text in Google Workspace Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting). |  [optional] |
|**topLabel** | **String** | The text that appears above &#x60;text&#x60;. Always truncates. |  [optional] |
|**wrapText** | **Boolean** | The wrap text setting. If &#x60;true&#x60;, the text wraps and displays on multiple lines. Otherwise, the text is truncated. Only applies to &#x60;text&#x60;, not &#x60;topLabel&#x60; and &#x60;bottomLabel&#x60;. |  [optional] |



