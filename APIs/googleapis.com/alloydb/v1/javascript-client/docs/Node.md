# AlloyDbApi.Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The identifier of the VM e.g. \&quot;test-read-0601-407e52be-ms3l\&quot;. | [optional] 
**ip** | **String** | The private IP address of the VM e.g. \&quot;10.57.0.34\&quot;. | [optional] 
**state** | **String** | Determined by state of the compute VM and postgres-service health. Compute VM state can have values listed in https://cloud.google.com/compute/docs/instances/instance-life-cycle and postgres-service health can have values: HEALTHY and UNHEALTHY. | [optional] 
**zoneId** | **String** | The Compute Engine zone of the VM e.g. \&quot;us-central1-b\&quot;. | [optional] 


