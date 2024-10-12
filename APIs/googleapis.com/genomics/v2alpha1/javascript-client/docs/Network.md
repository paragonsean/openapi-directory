# GenomicsApi.Network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The network name to attach the VM&#39;s network interface to. The value will be prefixed with &#x60;global/networks/&#x60; unless it contains a &#x60;/&#x60;, in which case it is assumed to be a fully specified network resource URL. If unspecified, the global default network is used. | [optional] 
**subnetwork** | **String** | If the specified network is configured for custom subnet creation, the name of the subnetwork to attach the instance to must be specified here. The value is prefixed with &#x60;regions/_*_/subnetworks/&#x60; unless it contains a &#x60;/&#x60;, in which case it is assumed to be a fully specified subnetwork resource URL. If the &#x60;*&#x60; character appears in the value, it is replaced with the region that the virtual machine has been allocated in. | [optional] 
**usePrivateAddress** | **Boolean** | If set to true, do not attach a public IP address to the VM. Note that without a public IP address, additional configuration is required to allow the VM to access Google services. See https://cloud.google.com/vpc/docs/configure-private-google-access for more information. | [optional] 


