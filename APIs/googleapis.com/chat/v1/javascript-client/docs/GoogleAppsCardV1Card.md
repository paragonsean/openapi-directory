# GoogleChatApi.GoogleAppsCardV1Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardActions** | [**[GoogleAppsCardV1CardAction]**](GoogleAppsCardV1CardAction.md) | The card&#39;s actions. Actions are added to the card&#39;s toolbar menu. [Google Workspace Add-ons](https://developers.google.com/workspace/add-ons): For example, the following JSON constructs a card action menu with &#x60;Settings&#x60; and &#x60;Send Feedback&#x60; options: &#x60;&#x60;&#x60; \&quot;card_actions\&quot;: [ { \&quot;actionLabel\&quot;: \&quot;Settings\&quot;, \&quot;onClick\&quot;: { \&quot;action\&quot;: { \&quot;functionName\&quot;: \&quot;goToView\&quot;, \&quot;parameters\&quot;: [ { \&quot;key\&quot;: \&quot;viewType\&quot;, \&quot;value\&quot;: \&quot;SETTING\&quot; } ], \&quot;loadIndicator\&quot;: \&quot;LoadIndicator.SPINNER\&quot; } } }, { \&quot;actionLabel\&quot;: \&quot;Send Feedback\&quot;, \&quot;onClick\&quot;: { \&quot;openLink\&quot;: { \&quot;url\&quot;: \&quot;https://example.com/feedback\&quot; } } } ] &#x60;&#x60;&#x60; | [optional] 
**displayStyle** | **String** | In Google Workspace Add-ons, sets the display properties of the &#x60;peekCardHeader&#x60;. [Google Workspace Add-ons](https://developers.google.com/workspace/add-ons): | [optional] 
**fixedFooter** | [**GoogleAppsCardV1CardFixedFooter**](GoogleAppsCardV1CardFixedFooter.md) |  | [optional] 
**header** | [**GoogleAppsCardV1CardHeader**](GoogleAppsCardV1CardHeader.md) |  | [optional] 
**name** | **String** | Name of the card. Used as a card identifier in card navigation. [Google Workspace Add-ons](https://developers.google.com/workspace/add-ons): | [optional] 
**peekCardHeader** | [**GoogleAppsCardV1CardHeader**](GoogleAppsCardV1CardHeader.md) |  | [optional] 
**sectionDividerStyle** | **String** | The divider style between sections. | [optional] 
**sections** | [**[GoogleAppsCardV1Section]**](GoogleAppsCardV1Section.md) | Contains a collection of widgets. Each section has its own, optional header. Sections are visually separated by a line divider. For an example in Google Chat apps, see [Card section](https://developers.google.com/chat/ui/widgets/card-section). | [optional] 



## Enum: DisplayStyleEnum


* `DISPLAY_STYLE_UNSPECIFIED` (value: `"DISPLAY_STYLE_UNSPECIFIED"`)

* `PEEK` (value: `"PEEK"`)

* `REPLACE` (value: `"REPLACE"`)





## Enum: SectionDividerStyleEnum


* `DIVIDER_STYLE_UNSPECIFIED` (value: `"DIVIDER_STYLE_UNSPECIFIED"`)

* `SOLID_DIVIDER` (value: `"SOLID_DIVIDER"`)

* `NO_DIVIDER` (value: `"NO_DIVIDER"`)




