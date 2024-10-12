

# ResolverQueryLogConfigAssociation

In the response to an <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverQueryLogConfig.html\">AssociateResolverQueryLogConfig</a>, <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html\">DisassociateResolverQueryLogConfig</a>, <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfigAssociation.html\">GetResolverQueryLogConfigAssociation</a>, or <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.html\">ListResolverQueryLogConfigAssociations</a>, request, a complex type that contains settings for a specified association between an Amazon VPC and a query logging configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**resolverQueryLogConfigId** | [**String**](String.md) |  |  [optional] |
|**resourceId** | [**String**](String.md) |  |  [optional] |
|**status** | [**ResolverQueryLogConfigAssociationStatus**](ResolverQueryLogConfigAssociationStatus.md) |  |  [optional] |
|**error** | [**ResolverQueryLogConfigAssociationError**](ResolverQueryLogConfigAssociationError.md) |  |  [optional] |
|**errorMessage** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**String**](String.md) |  |  [optional] |



