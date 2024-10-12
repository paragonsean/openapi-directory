

# GoogleCloudApigeeV1FlowHook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continueOnError** | **Boolean** | Optional. Flag that specifies whether execution should continue if the flow hook throws an exception. Set to &#x60;true&#x60; to continue execution. Set to &#x60;false&#x60; to stop execution if the flow hook throws an exception. Defaults to &#x60;true&#x60;. |  [optional] |
|**description** | **String** | Description of the flow hook. |  [optional] |
|**flowHookPoint** | **String** | Output only. Where in the API call flow the flow hook is invoked. Must be one of &#x60;PreProxyFlowHook&#x60;, &#x60;PostProxyFlowHook&#x60;, &#x60;PreTargetFlowHook&#x60;, or &#x60;PostTargetFlowHook&#x60;. |  [optional] [readonly] |
|**sharedFlow** | **String** | Shared flow attached to this flow hook, or empty if there is none attached. |  [optional] |



