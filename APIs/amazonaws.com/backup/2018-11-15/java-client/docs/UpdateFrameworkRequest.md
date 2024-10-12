

# UpdateFrameworkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frameworkDescription** | **String** | An optional description of the framework with a maximum 1,024 characters. |  [optional] |
|**frameworkControls** | [**List&lt;FrameworkControl&gt;**](FrameworkControl.md) | A list of the controls that make up the framework. Each control in the list has a name, input parameters, and scope. |  [optional] |
|**idempotencyToken** | **String** | A customer-chosen string that you can use to distinguish between otherwise identical calls to &lt;code&gt;UpdateFrameworkInput&lt;/code&gt;. Retrying a successful request with the same idempotency token results in a success message with no action taken. |  [optional] |



