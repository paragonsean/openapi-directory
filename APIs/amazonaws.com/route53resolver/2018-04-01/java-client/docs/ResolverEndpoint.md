

# ResolverEndpoint

In the response to a <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html\">CreateResolverEndpoint</a>, <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverEndpoint.html\">DeleteResolverEndpoint</a>, <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html\">GetResolverEndpoint</a>, Updates the name, or ResolverEndpointType for an endpoint, or <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverEndpoint.html\">UpdateResolverEndpoint</a> request, a complex type that contains settings for an existing inbound or outbound Resolver endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**creatorRequestId** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**securityGroupIds** | [**List**](List.md) |  |  [optional] |
|**direction** | [**ResolverEndpointDirection**](ResolverEndpointDirection.md) |  |  [optional] |
|**ipAddressCount** | [**Integer**](Integer.md) |  |  [optional] |
|**hostVPCId** | [**String**](String.md) |  |  [optional] |
|**status** | [**ResolverEndpointStatus**](ResolverEndpointStatus.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**String**](String.md) |  |  [optional] |
|**modificationTime** | [**String**](String.md) |  |  [optional] |
|**resolverEndpointType** | [**ResolverEndpointType**](ResolverEndpointType.md) |  |  [optional] |
|**outpostArn** | [**String**](String.md) |  |  [optional] |
|**preferredInstanceType** | [**String**](String.md) |  |  [optional] |



