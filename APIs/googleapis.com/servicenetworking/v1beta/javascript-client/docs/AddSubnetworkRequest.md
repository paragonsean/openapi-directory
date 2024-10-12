# ServiceNetworkingApi.AddSubnetworkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer** | **String** | Required. A resource that represents the service consumer, such as &#x60;projects/123456&#x60;. The project number can be different from the value in the consumer network parameter. For example, the network might be part of a Shared VPC network. In those cases, Service Networking validates that this resource belongs to that Shared VPC. | [optional] 
**consumerNetwork** | **String** | Required. The name of the service consumer&#39;s VPC network. The network must have an existing private connection that was provisioned through the connections.create method. The name must be in the following format: &#x60;projects/{project}/global/networks/{network}&#x60;, where {project} is a project number, such as &#x60;12345&#x60;. {network} is the name of a VPC network in the project. | [optional] 
**description** | **String** | An optional description of the subnet. | [optional] 
**ipPrefixLength** | **Number** | Required. The prefix length of the subnet&#39;s IP address range. Use CIDR range notation, such as &#x60;30&#x60; to provision a subnet with an &#x60;x.x.x.x/30&#x60; CIDR range. The IP address range is drawn from a pool of available ranges in the service consumer&#39;s allocated range. | [optional] 
**region** | **String** | Required. The name of a [region](/compute/docs/regions-zones) for the subnet, such &#x60;europe-west1&#x60;. | [optional] 
**requestedAddress** | **String** | Optional. The starting address of a range. The address must be a valid IPv4 address in the x.x.x.x format. This value combined with the IP prefix range is the CIDR range for the subnet. The range must be within the allocated range that is assigned to the private connection. If the CIDR range isn&#39;t available, the call fails. | [optional] 
**subnetwork** | **String** | Required. A name for the new subnet. For information about the naming requirements, see [subnetwork](/compute/docs/reference/rest/v1/subnetworks) in the Compute API documentation. | [optional] 
**subnetworkUsers** | **[String]** | A list of members that are granted the &#x60;compute.networkUser&#x60; role on the subnet. | [optional] 


