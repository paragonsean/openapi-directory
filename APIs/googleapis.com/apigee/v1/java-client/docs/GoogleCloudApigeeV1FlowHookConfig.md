

# GoogleCloudApigeeV1FlowHookConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continueOnError** | **Boolean** | Flag that specifies whether the flow should abort after an error in the flow hook. Defaults to &#x60;true&#x60; (continue on error). |  [optional] |
|**name** | **String** | Name of the flow hook in the following format: &#x60;organizations/{org}/environments/{env}/flowhooks/{point}&#x60;. Valid &#x60;point&#x60; values include: &#x60;PreProxyFlowHook&#x60;, &#x60;PostProxyFlowHook&#x60;, &#x60;PreTargetFlowHook&#x60;, and &#x60;PostTargetFlowHook&#x60; |  [optional] |
|**sharedFlowName** | **String** | Name of the shared flow to invoke in the following format: &#x60;organizations/{org}/sharedflows/{sharedflow}&#x60; |  [optional] |



