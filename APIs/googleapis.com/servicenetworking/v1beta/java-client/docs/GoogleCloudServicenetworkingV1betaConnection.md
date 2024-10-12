

# GoogleCloudServicenetworkingV1betaConnection

Represents a private connection resource. A private connection is implemented as a VPC Network Peering connection between a service producer's VPC network and a service consumer's VPC network.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**network** | **String** | The name of service consumer&#39;s VPC network that&#39;s connected with service producer network, in the following format: &#x60;projects/{project}/global/networks/{network}&#x60;. &#x60;{project}&#x60; is a project number, such as in &#x60;12345&#x60; that includes the VPC service consumer&#39;s VPC network. &#x60;{network}&#x60; is the name of the service consumer&#39;s VPC network. |  [optional] |
|**peering** | **String** | Output only. The name of the VPC Network Peering connection that was created by the service producer. |  [optional] |
|**reservedPeeringRanges** | **List&lt;String&gt;** | The name of one or more allocated IP address ranges for this service producer of type &#x60;PEERING&#x60;. Note that invoking this method with a different range when connection is already established will not modify already provisioned service producer subnetworks. |  [optional] |
|**service** | **String** | Output only. The name of the peering service that&#39;s associated with this connection, in the following format: &#x60;services/{service name}&#x60;. |  [optional] |



