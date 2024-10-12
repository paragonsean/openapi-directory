

# EvaluateCodeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**runtime** | [**CreateFunctionRequestRuntime**](CreateFunctionRequestRuntime.md) |  |  |
|**code** | **String** | The code definition to be evaluated. Note that &lt;code&gt;code&lt;/code&gt; and &lt;code&gt;runtime&lt;/code&gt; are both required for this action. The &lt;code&gt;runtime&lt;/code&gt; value must be &lt;code&gt;APPSYNC_JS&lt;/code&gt;. |  |
|**context** | **String** | The map that holds all of the contextual information for your resolver invocation. A &lt;code&gt;context&lt;/code&gt; is required for this action. |  |
|**function** | **String** | The function within the code to be evaluated. If provided, the valid values are &lt;code&gt;request&lt;/code&gt; and &lt;code&gt;response&lt;/code&gt;. |  [optional] |



