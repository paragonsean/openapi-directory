# WorkflowExecutionsApi.Callback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availablePayloads** | **[String]** | Output only. The payloads received by the callback that have not been processed by a waiting execution step. | [optional] [readonly] 
**method** | **String** | Output only. The method accepted by the callback. For example: GET, POST, PUT. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the callback. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}/callback/{callback} | [optional] [readonly] 
**waiters** | **String** | Output only. Number of execution steps waiting on this callback. | [optional] [readonly] 


