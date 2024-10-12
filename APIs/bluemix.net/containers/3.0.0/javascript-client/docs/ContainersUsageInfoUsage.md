# IbmContainersApi.ContainersUsageInfoUsage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | **Number** | The number of containers that were created in the space. All containers that count towards the quota limit are listed independent on their current state. | [optional] 
**floatingIps** | **Number** | The number of public IP addresses that are allocated to the space. | [optional] 
**floatingIpsBound** | **Number** | The number of public IP addresses that are bound to a container in the space. | [optional] 
**images** | **Number** | The number of private images that were added to the private Bluemix registry. | [optional] 
**memoryMB** | **Number** | The amount of container memory that is already used by the containers that were created in the space in megabyte. | [optional] 
**running** | **Number** | The number of containers that are currently in a running state. | [optional] 
**vcpu** | **Number** | The number of virtual CPUs that are allocated to the space. | [optional] 


