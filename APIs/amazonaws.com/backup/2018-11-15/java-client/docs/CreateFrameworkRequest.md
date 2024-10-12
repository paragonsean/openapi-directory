

# CreateFrameworkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frameworkName** | **String** | The unique name of the framework. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_). |  |
|**frameworkDescription** | **String** | An optional description of the framework with a maximum of 1,024 characters. |  [optional] |
|**frameworkControls** | [**List&lt;FrameworkControl&gt;**](FrameworkControl.md) | A list of the controls that make up the framework. Each control in the list has a name, input parameters, and scope. |  |
|**idempotencyToken** | **String** | A customer-chosen string that you can use to distinguish between otherwise identical calls to &lt;code&gt;CreateFrameworkInput&lt;/code&gt;. Retrying a successful request with the same idempotency token results in a success message with no action taken. |  [optional] |
|**frameworkTags** | **Map&lt;String, String&gt;** | Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair. |  [optional] |



