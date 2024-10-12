# RemoteBuildExecutionApi.GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxSize** | **String** | Optional. The maximal number of workers. Must be equal to or greater than min_size. | [optional] 
**minIdleWorkers** | **String** | Optional. The minimum number of idle workers the autoscaler will aim to have in the pool at all times that are immediately available to accept a surge in build traffic. The pool size will still be constrained by min_size and max_size. | [optional] 
**minSize** | **String** | Optional. The minimal number of workers. Must be greater than 0. | [optional] 


