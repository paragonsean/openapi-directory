# AzureMachineLearningWorkspaces.AksNetworkingConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsServiceIP** | **String** | An IP address assigned to the Kubernetes DNS service. It must be within the Kubernetes service address range specified in serviceCidr. | [optional] 
**dockerBridgeCidr** | **String** | A CIDR notation IP range assigned to the Docker bridge network. It must not overlap with any Subnet IP ranges or the Kubernetes service address range. | [optional] 
**serviceCidr** | **String** | A CIDR notation IP range from which to assign service cluster IPs. It must not overlap with any Subnet IP ranges. | [optional] 
**subnetId** | **String** | Virtual network subnet resource ID the compute nodes belong to | [optional] 


