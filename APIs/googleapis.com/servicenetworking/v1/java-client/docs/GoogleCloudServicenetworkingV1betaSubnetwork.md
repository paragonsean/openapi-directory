

# GoogleCloudServicenetworkingV1betaSubnetwork

Represents a subnet that was created or discovered by a private access management service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipCidrRange** | **String** | Subnetwork CIDR range in &#x60;10.x.x.x/y&#x60; format. |  [optional] |
|**name** | **String** | Subnetwork name. See https://cloud.google.com/compute/docs/vpc/ |  [optional] |
|**network** | **String** | In the Shared VPC host project, the VPC network that&#39;s peered with the consumer network. For example: &#x60;projects/1234321/global/networks/host-network&#x60; |  [optional] |
|**outsideAllocation** | **Boolean** | This is a discovered subnet that is not within the current consumer allocated ranges. |  [optional] |



