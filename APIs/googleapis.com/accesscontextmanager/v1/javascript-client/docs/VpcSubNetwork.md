# AccessContextManagerApi.VpcSubNetwork

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **String** | Required. Network name. If the network is not part of the organization, the &#x60;compute.network.get&#x60; permission must be granted to the caller. Format: &#x60;//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NETWORK_NAME}&#x60; Example: &#x60;//compute.googleapis.com/projects/my-project/global/networks/network-1&#x60; | [optional] 
**vpcIpSubnetworks** | **[String]** | CIDR block IP subnetwork specification. The IP address must be an IPv4 address and can be a public or private IP address. Note that for a CIDR IP address block, the specified IP address portion must be properly truncated (i.e. all the host bits must be zero) or the input is considered malformed. For example, \&quot;192.0.2.0/24\&quot; is accepted but \&quot;192.0.2.1/24\&quot; is not. If empty, all IP addresses are allowed. | [optional] 


