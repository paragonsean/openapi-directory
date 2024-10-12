

# CommonEventObject

Represents information about the user's client, such as locale, host app, and platform. For Chat apps, `CommonEventObject` includes data submitted by users interacting with cards, like data entered in [dialogs](https://developers.google.com/chat/how-tos/dialogs).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formInputs** | [**Map&lt;String, Inputs&gt;**](Inputs.md) | A map containing the values that a user inputs in a widget from a card or dialog. The map keys are the string IDs assigned to each widget, and the values represent inputs to the widget. For details, see [Process information inputted by users](https://developers.google.com/chat/ui/read-form-data). |  [optional] |
|**hostApp** | [**HostAppEnum**](#HostAppEnum) | The hostApp enum which indicates the app the add-on is invoked from. Always &#x60;CHAT&#x60; for Chat apps. |  [optional] |
|**invokedFunction** | **String** | Name of the invoked function associated with the widget. Only set for Chat apps. |  [optional] |
|**parameters** | **Map&lt;String, String&gt;** | Custom [parameters](/chat/api/reference/rest/v1/cards#ActionParameter) passed to the invoked function. Both keys and values must be strings. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | The platform enum which indicates the platform where the event originates (&#x60;WEB&#x60;, &#x60;IOS&#x60;, or &#x60;ANDROID&#x60;). Not supported by Chat apps. |  [optional] |
|**timeZone** | [**TimeZone**](TimeZone.md) |  |  [optional] |
|**userLocale** | **String** | The full &#x60;locale.displayName&#x60; in the format of [ISO 639 language code]-[ISO 3166 country/region code] such as \&quot;en-US\&quot;. |  [optional] |



## Enum: HostAppEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED_HOST_APP | &quot;UNSPECIFIED_HOST_APP&quot; |
| GMAIL | &quot;GMAIL&quot; |
| CALENDAR | &quot;CALENDAR&quot; |
| DRIVE | &quot;DRIVE&quot; |
| DEMO | &quot;DEMO&quot; |
| DOCS | &quot;DOCS&quot; |
| MEET | &quot;MEET&quot; |
| SHEETS | &quot;SHEETS&quot; |
| SLIDES | &quot;SLIDES&quot; |
| DRAWINGS | &quot;DRAWINGS&quot; |
| CHAT | &quot;CHAT&quot; |
| CHAT_IN_GMAIL | &quot;CHAT_IN_GMAIL&quot; |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| UNKNOWN_PLATFORM | &quot;UNKNOWN_PLATFORM&quot; |
| WEB | &quot;WEB&quot; |
| IOS | &quot;IOS&quot; |
| ANDROID | &quot;ANDROID&quot; |



