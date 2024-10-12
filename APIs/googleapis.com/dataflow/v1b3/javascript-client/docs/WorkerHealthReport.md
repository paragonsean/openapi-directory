# DataflowApi.WorkerHealthReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **String** | Message describing any unusual health reports. | [optional] 
**pods** | **[{String: Object}]** | The pods running on the worker. See: http://kubernetes.io/v1.1/docs/api-reference/v1/definitions.html#_v1_pod This field is used by the worker to send the status of the indvidual containers running on each worker. | [optional] 
**reportInterval** | **String** | The interval at which the worker is sending health reports. The default value of 0 should be interpreted as the field is not being explicitly set by the worker. | [optional] 
**vmBrokenCode** | **String** | Code to describe a specific reason, if known, that a VM has reported broken state. | [optional] 
**vmIsBroken** | **Boolean** | Whether the VM is in a permanently broken state. Broken VMs should be abandoned or deleted ASAP to avoid assigning or completing any work. | [optional] 
**vmIsHealthy** | **Boolean** | Whether the VM is currently healthy. | [optional] 
**vmStartupTime** | **String** | The time the VM was booted. | [optional] 


