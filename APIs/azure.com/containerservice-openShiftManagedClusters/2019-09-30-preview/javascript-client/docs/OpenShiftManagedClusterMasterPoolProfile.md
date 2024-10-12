# ContainerServiceClient.OpenShiftManagedClusterMasterPoolProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | Number of masters (VMs) to host docker containers. The default value is 3. | 
**name** | **String** | Unique name of the master pool profile in the context of the subscription and resource group. | [optional] 
**osType** | [**OSType**](OSType.md) |  | [optional] 
**subnetCidr** | **String** | Subnet CIDR for the peering. | [optional] 
**vmSize** | [**OpenShiftContainerServiceVMSize**](OpenShiftContainerServiceVMSize.md) |  | 


