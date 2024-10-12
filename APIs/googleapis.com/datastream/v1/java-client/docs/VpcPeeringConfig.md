

# VpcPeeringConfig

The VPC Peering configuration is used to create VPC peering between Datastream and the consumer's VPC.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**subnet** | **String** | Required. A free subnet for peering. (CIDR of /29) |  [optional] |
|**vpc** | **String** | Required. Fully qualified name of the VPC that Datastream will peer to. Format: &#x60;projects/{project}/global/{networks}/{name}&#x60; |  [optional] |



