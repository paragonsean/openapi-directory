# GoogleChatApi.GoogleAppsCardV1Action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_function** | **String** | A custom function to invoke when the containing element is clicked or othrwise activated. For example usage, see [Create interactive cards](https://developers.google.com/chat/how-tos/cards-onclick). | [optional] 
**interaction** | **String** | Optional. Required when opening a [dialog](https://developers.google.com/chat/how-tos/dialogs). What to do in response to an interaction with a user, such as a user clicking a button in a card message. If unspecified, the app responds by executing an &#x60;action&#x60;—like opening a link or running a function—as normal. By specifying an &#x60;interaction&#x60;, the app can respond in special interactive ways. For example, by setting &#x60;interaction&#x60; to &#x60;OPEN_DIALOG&#x60;, the app can open a [dialog](https://developers.google.com/chat/how-tos/dialogs). When specified, a loading indicator isn&#39;t shown. If specified for an add-on, the entire card is stripped and nothing is shown in the client. [Google Chat apps](https://developers.google.com/chat): | [optional] 
**loadIndicator** | **String** | Specifies the loading indicator that the action displays while making the call to the action. | [optional] 
**parameters** | [**[GoogleAppsCardV1ActionParameter]**](GoogleAppsCardV1ActionParameter.md) | List of action parameters. | [optional] 
**persistValues** | **Boolean** | Indicates whether form values persist after the action. The default value is &#x60;false&#x60;. If &#x60;true&#x60;, form values remain after the action is triggered. To let the user make changes while the action is being processed, set [&#x60;LoadIndicator&#x60;](https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator) to &#x60;NONE&#x60;. For [card messages](https://developers.google.com/chat/api/guides/v1/messages/create#create) in Chat apps, you must also set the action&#39;s [&#x60;ResponseType&#x60;](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages#responsetype) to &#x60;UPDATE_MESSAGE&#x60; and use the same [&#x60;card_id&#x60;](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages#CardWithId) from the card that contained the action. If &#x60;false&#x60;, the form values are cleared when the action is triggered. To prevent the user from making changes while the action is being processed, set [&#x60;LoadIndicator&#x60;](https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator) to &#x60;SPINNER&#x60;. | [optional] 



## Enum: InteractionEnum


* `INTERACTION_UNSPECIFIED` (value: `"INTERACTION_UNSPECIFIED"`)

* `OPEN_DIALOG` (value: `"OPEN_DIALOG"`)





## Enum: LoadIndicatorEnum


* `SPINNER` (value: `"SPINNER"`)

* `NONE` (value: `"NONE"`)




