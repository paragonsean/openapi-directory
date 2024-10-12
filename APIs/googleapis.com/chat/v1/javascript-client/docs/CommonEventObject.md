# GoogleChatApi.CommonEventObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formInputs** | [**{String: Inputs}**](Inputs.md) | A map containing the values that a user inputs in a widget from a card or dialog. The map keys are the string IDs assigned to each widget, and the values represent inputs to the widget. For details, see [Process information inputted by users](https://developers.google.com/chat/ui/read-form-data). | [optional] 
**hostApp** | **String** | The hostApp enum which indicates the app the add-on is invoked from. Always &#x60;CHAT&#x60; for Chat apps. | [optional] 
**invokedFunction** | **String** | Name of the invoked function associated with the widget. Only set for Chat apps. | [optional] 
**parameters** | **{String: String}** | Custom [parameters](/chat/api/reference/rest/v1/cards#ActionParameter) passed to the invoked function. Both keys and values must be strings. | [optional] 
**platform** | **String** | The platform enum which indicates the platform where the event originates (&#x60;WEB&#x60;, &#x60;IOS&#x60;, or &#x60;ANDROID&#x60;). Not supported by Chat apps. | [optional] 
**timeZone** | [**TimeZone**](TimeZone.md) |  | [optional] 
**userLocale** | **String** | The full &#x60;locale.displayName&#x60; in the format of [ISO 639 language code]-[ISO 3166 country/region code] such as \&quot;en-US\&quot;. | [optional] 



## Enum: HostAppEnum


* `UNSPECIFIED_HOST_APP` (value: `"UNSPECIFIED_HOST_APP"`)

* `GMAIL` (value: `"GMAIL"`)

* `CALENDAR` (value: `"CALENDAR"`)

* `DRIVE` (value: `"DRIVE"`)

* `DEMO` (value: `"DEMO"`)

* `DOCS` (value: `"DOCS"`)

* `MEET` (value: `"MEET"`)

* `SHEETS` (value: `"SHEETS"`)

* `SLIDES` (value: `"SLIDES"`)

* `DRAWINGS` (value: `"DRAWINGS"`)

* `CHAT` (value: `"CHAT"`)

* `CHAT_IN_GMAIL` (value: `"CHAT_IN_GMAIL"`)





## Enum: PlatformEnum


* `UNKNOWN_PLATFORM` (value: `"UNKNOWN_PLATFORM"`)

* `WEB` (value: `"WEB"`)

* `IOS` (value: `"IOS"`)

* `ANDROID` (value: `"ANDROID"`)




