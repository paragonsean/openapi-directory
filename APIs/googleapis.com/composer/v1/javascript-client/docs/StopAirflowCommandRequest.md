# CloudComposerApi.StopAirflowCommandRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionId** | **String** | The unique ID of the command execution. | [optional] 
**force** | **Boolean** | If true, the execution is terminated forcefully (SIGKILL). If false, the execution is stopped gracefully, giving it time for cleanup. | [optional] 
**pod** | **String** | The name of the pod where the command is executed. | [optional] 
**podNamespace** | **String** | The namespace of the pod where the command is executed. | [optional] 


