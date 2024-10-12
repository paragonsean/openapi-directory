

# FormAction

A form action describes the behavior when the form is submitted. For example, you can invoke Apps Script to handle the form.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionMethodName** | **String** | The method name is used to identify which part of the form triggered the form submission. This information is echoed back to the Chat app as part of the card click event. You can use the same method name for several elements that trigger a common behavior. |  [optional] |
|**parameters** | [**List&lt;ActionParameter&gt;**](ActionParameter.md) | List of action parameters. |  [optional] |



