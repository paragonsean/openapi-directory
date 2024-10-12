# AppsScriptApi.ExecutionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devMode** | **Boolean** | If &#x60;true&#x60; and the user is an owner of the script, the script runs at the most recently saved version rather than the version deployed for use with the Apps Script API. Optional; default is &#x60;false&#x60;. | [optional] 
**_function** | **String** | The name of the function to execute in the given script. The name does not include parentheses or parameters. It can reference a function in an included library such as &#x60;Library.libFunction1&#x60;. | [optional] 
**parameters** | **[Object]** | The parameters to be passed to the function being executed. The object type for each parameter should match the expected type in Apps Script. Parameters cannot be Apps Script-specific object types (such as a &#x60;Document&#x60; or a &#x60;Calendar&#x60;); they can only be primitive types such as &#x60;string&#x60;, &#x60;number&#x60;, &#x60;array&#x60;, &#x60;object&#x60;, or &#x60;boolean&#x60;. Optional. | [optional] 
**sessionState** | **String** | *Deprecated*. For use with Android add-ons only. An ID that represents the user&#39;s current session in the Android app for Google Docs or Sheets, included as extra data in the [Intent](https://developer.android.com/guide/components/intents-filters.html) that launches the add-on. When an Android add-on is run with a session state, it gains the privileges of a [bound](https://developers.google.com/apps-script/guides/bound) script—that is, it can access information like the user&#39;s current cursor position (in Docs) or selected cell (in Sheets). To retrieve the state, call &#x60;Intent.getStringExtra(\&quot;com.google.android.apps.docs.addons.SessionState\&quot;)&#x60;. Optional. | [optional] 


