

# RoboDirective

Directs Robo to interact with a specific UI element if it is encountered during the crawl. Currently, Robo can perform text entry or element click.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | Required. The type of action that Robo should perform on the specified element. |  [optional] |
|**inputText** | **String** | The text that Robo is directed to set. If left empty, the directive will be treated as a CLICK on the element matching the resource_name. |  [optional] |
|**resourceName** | **String** | Required. The android resource name of the target UI element. For example, in Java: R.string.foo in xml: @string/foo Only the \&quot;foo\&quot; part is needed. Reference doc: https://developer.android.com/guide/topics/resources/accessing-resources.html |  [optional] |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| ACTION_TYPE_UNSPECIFIED | &quot;ACTION_TYPE_UNSPECIFIED&quot; |
| SINGLE_CLICK | &quot;SINGLE_CLICK&quot; |
| ENTER_TEXT | &quot;ENTER_TEXT&quot; |
| IGNORE | &quot;IGNORE&quot; |



