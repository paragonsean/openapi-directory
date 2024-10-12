

# KeyValue

A UI element contains a key (label) and a value (content). This element can also contain some actions such as `onclick` button.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bottomLabel** | **String** | The text of the bottom label. Formatted text supported. For more information about formatting text, see [Formatting text in Google Chat apps](https://developers.google.com/chat/format-messages#card-formatting) and [Formatting text in Google Workspace Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting). |  [optional] |
|**button** | [**Button**](Button.md) |  |  [optional] |
|**content** | **String** | The text of the content. Formatted text supported and always required. For more information about formatting text, see [Formatting text in Google Chat apps](https://developers.google.com/chat/format-messages#card-formatting) and [Formatting text in Google Workspace Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting). |  [optional] |
|**contentMultiline** | **Boolean** | If the content should be multiline. |  [optional] |
|**icon** | [**IconEnum**](#IconEnum) | An enum value that&#39;s replaced by the Chat API with the corresponding icon image. |  [optional] |
|**iconUrl** | **String** | The icon specified by a URL. |  [optional] |
|**onClick** | [**OnClick**](OnClick.md) |  |  [optional] |
|**topLabel** | **String** | The text of the top label. Formatted text supported. For more information about formatting text, see [Formatting text in Google Chat apps](https://developers.google.com/chat/format-messages#card-formatting) and [Formatting text in Google Workspace Add-ons](https://developers.google.com/apps-script/add-ons/concepts/widgets#text_formatting). |  [optional] |



## Enum: IconEnum

| Name | Value |
|---- | -----|
| ICON_UNSPECIFIED | &quot;ICON_UNSPECIFIED&quot; |
| AIRPLANE | &quot;AIRPLANE&quot; |
| BOOKMARK | &quot;BOOKMARK&quot; |
| BUS | &quot;BUS&quot; |
| CAR | &quot;CAR&quot; |
| CLOCK | &quot;CLOCK&quot; |
| CONFIRMATION_NUMBER_ICON | &quot;CONFIRMATION_NUMBER_ICON&quot; |
| DOLLAR | &quot;DOLLAR&quot; |
| DESCRIPTION | &quot;DESCRIPTION&quot; |
| EMAIL | &quot;EMAIL&quot; |
| EVENT_PERFORMER | &quot;EVENT_PERFORMER&quot; |
| EVENT_SEAT | &quot;EVENT_SEAT&quot; |
| FLIGHT_ARRIVAL | &quot;FLIGHT_ARRIVAL&quot; |
| FLIGHT_DEPARTURE | &quot;FLIGHT_DEPARTURE&quot; |
| HOTEL | &quot;HOTEL&quot; |
| HOTEL_ROOM_TYPE | &quot;HOTEL_ROOM_TYPE&quot; |
| INVITE | &quot;INVITE&quot; |
| MAP_PIN | &quot;MAP_PIN&quot; |
| MEMBERSHIP | &quot;MEMBERSHIP&quot; |
| MULTIPLE_PEOPLE | &quot;MULTIPLE_PEOPLE&quot; |
| OFFER | &quot;OFFER&quot; |
| PERSON | &quot;PERSON&quot; |
| PHONE | &quot;PHONE&quot; |
| RESTAURANT_ICON | &quot;RESTAURANT_ICON&quot; |
| SHOPPING_CART | &quot;SHOPPING_CART&quot; |
| STAR | &quot;STAR&quot; |
| STORE | &quot;STORE&quot; |
| TICKET | &quot;TICKET&quot; |
| TRAIN | &quot;TRAIN&quot; |
| VIDEO_CAMERA | &quot;VIDEO_CAMERA&quot; |
| VIDEO_PLAY | &quot;VIDEO_PLAY&quot; |



