# CloudTestingApi.RoboDirective

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionType** | **String** | Required. The type of action that Robo should perform on the specified element. | [optional] 
**inputText** | **String** | The text that Robo is directed to set. If left empty, the directive will be treated as a CLICK on the element matching the resource_name. | [optional] 
**resourceName** | **String** | Required. The android resource name of the target UI element. For example, in Java: R.string.foo in xml: @string/foo Only the \&quot;foo\&quot; part is needed. Reference doc: https://developer.android.com/guide/topics/resources/accessing-resources.html | [optional] 



## Enum: ActionTypeEnum


* `ACTION_TYPE_UNSPECIFIED` (value: `"ACTION_TYPE_UNSPECIFIED"`)

* `SINGLE_CLICK` (value: `"SINGLE_CLICK"`)

* `ENTER_TEXT` (value: `"ENTER_TEXT"`)

* `IGNORE` (value: `"IGNORE"`)




