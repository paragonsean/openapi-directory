

# GoogleAppsCardV1Card

A card interface displayed in a Google Chat message or Google Workspace Add-on. Cards support a defined layout, interactive UI elements like buttons, and rich media like images. Use cards to present detailed information, gather information from users, and guide users to take a next step. [Card builder](https://addons.gsuite.google.com/uikit/builder) To learn how to build cards, see the following documentation: * For Google Chat apps, see [Design dynamic, interactive, and consistent UIs with cards](https://developers.google.com/chat/ui). * For Google Workspace Add-ons, see [Card-based interfaces](https://developers.google.com/apps-script/add-ons/concepts/cards). **Example: Card message for a Google Chat app** ![Example contact card](https://developers.google.com/chat/images/card_api_reference.png) To create the sample card message in Google Chat, use the following JSON: ``` { \"cardsV2\": [ { \"cardId\": \"unique-card-id\", \"card\": { \"header\": { \"title\": \"Sasha\", \"subtitle\": \"Software Engineer\", \"imageUrl\": \"https://developers.google.com/chat/images/quickstart-app-avatar.png\", \"imageType\": \"CIRCLE\", \"imageAltText\": \"Avatar for Sasha\", }, \"sections\": [ { \"header\": \"Contact Info\", \"collapsible\": true, \"uncollapsibleWidgetsCount\": 1, \"widgets\": [ { \"decoratedText\": { \"startIcon\": { \"knownIcon\": \"EMAIL\", }, \"text\": \"sasha@example.com\", } }, { \"decoratedText\": { \"startIcon\": { \"knownIcon\": \"PERSON\", }, \"text\": \"Online\", }, }, { \"decoratedText\": { \"startIcon\": { \"knownIcon\": \"PHONE\", }, \"text\": \"+1 (555) 555-1234\", } }, { \"buttonList\": { \"buttons\": [ { \"text\": \"Share\", \"onClick\": { \"openLink\": { \"url\": \"https://example.com/share\", } } }, { \"text\": \"Edit\", \"onClick\": { \"action\": { \"function\": \"goToView\", \"parameters\": [ { \"key\": \"viewType\", \"value\": \"EDIT\", } ], } } }, ], } }, ], }, ], }, } ], } ```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardActions** | [**List&lt;GoogleAppsCardV1CardAction&gt;**](GoogleAppsCardV1CardAction.md) | The card&#39;s actions. Actions are added to the card&#39;s toolbar menu. [Google Workspace Add-ons](https://developers.google.com/workspace/add-ons): For example, the following JSON constructs a card action menu with &#x60;Settings&#x60; and &#x60;Send Feedback&#x60; options: &#x60;&#x60;&#x60; \&quot;card_actions\&quot;: [ { \&quot;actionLabel\&quot;: \&quot;Settings\&quot;, \&quot;onClick\&quot;: { \&quot;action\&quot;: { \&quot;functionName\&quot;: \&quot;goToView\&quot;, \&quot;parameters\&quot;: [ { \&quot;key\&quot;: \&quot;viewType\&quot;, \&quot;value\&quot;: \&quot;SETTING\&quot; } ], \&quot;loadIndicator\&quot;: \&quot;LoadIndicator.SPINNER\&quot; } } }, { \&quot;actionLabel\&quot;: \&quot;Send Feedback\&quot;, \&quot;onClick\&quot;: { \&quot;openLink\&quot;: { \&quot;url\&quot;: \&quot;https://example.com/feedback\&quot; } } } ] &#x60;&#x60;&#x60; |  [optional] |
|**displayStyle** | [**DisplayStyleEnum**](#DisplayStyleEnum) | In Google Workspace Add-ons, sets the display properties of the &#x60;peekCardHeader&#x60;. [Google Workspace Add-ons](https://developers.google.com/workspace/add-ons): |  [optional] |
|**fixedFooter** | [**GoogleAppsCardV1CardFixedFooter**](GoogleAppsCardV1CardFixedFooter.md) |  |  [optional] |
|**header** | [**GoogleAppsCardV1CardHeader**](GoogleAppsCardV1CardHeader.md) |  |  [optional] |
|**name** | **String** | Name of the card. Used as a card identifier in card navigation. [Google Workspace Add-ons](https://developers.google.com/workspace/add-ons): |  [optional] |
|**peekCardHeader** | [**GoogleAppsCardV1CardHeader**](GoogleAppsCardV1CardHeader.md) |  |  [optional] |
|**sectionDividerStyle** | [**SectionDividerStyleEnum**](#SectionDividerStyleEnum) | The divider style between sections. |  [optional] |
|**sections** | [**List&lt;GoogleAppsCardV1Section&gt;**](GoogleAppsCardV1Section.md) | Contains a collection of widgets. Each section has its own, optional header. Sections are visually separated by a line divider. For an example in Google Chat apps, see [Card section](https://developers.google.com/chat/ui/widgets/card-section). |  [optional] |



## Enum: DisplayStyleEnum

| Name | Value |
|---- | -----|
| DISPLAY_STYLE_UNSPECIFIED | &quot;DISPLAY_STYLE_UNSPECIFIED&quot; |
| PEEK | &quot;PEEK&quot; |
| REPLACE | &quot;REPLACE&quot; |



## Enum: SectionDividerStyleEnum

| Name | Value |
|---- | -----|
| DIVIDER_STYLE_UNSPECIFIED | &quot;DIVIDER_STYLE_UNSPECIFIED&quot; |
| SOLID_DIVIDER | &quot;SOLID_DIVIDER&quot; |
| NO_DIVIDER | &quot;NO_DIVIDER&quot; |



