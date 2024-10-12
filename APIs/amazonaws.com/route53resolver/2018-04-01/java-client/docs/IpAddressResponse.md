

# IpAddressResponse

In the response to a <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html\">GetResolverEndpoint</a> request, information about the IP addresses that the Resolver endpoint uses for DNS queries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipId** | [**String**](String.md) |  |  [optional] |
|**subnetId** | [**String**](String.md) |  |  [optional] |
|**ip** | [**String**](String.md) |  |  [optional] |
|**ipv6** | [**String**](String.md) |  |  [optional] |
|**status** | [**IpAddressStatus**](IpAddressStatus.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**String**](String.md) |  |  [optional] |
|**modificationTime** | [**String**](String.md) |  |  [optional] |



