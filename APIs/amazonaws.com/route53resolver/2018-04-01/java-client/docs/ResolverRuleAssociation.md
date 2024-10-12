

# ResolverRuleAssociation

In the response to an <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html\">AssociateResolverRule</a>, <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverRule.html\">DisassociateResolverRule</a>, or <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html\">ListResolverRuleAssociations</a> request, provides information about an association between a Resolver rule and a VPC. The association determines which DNS queries that originate in the VPC are forwarded to your network. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**resolverRuleId** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**vpCId** | [**String**](String.md) |  |  [optional] |
|**status** | [**ResolverRuleAssociationStatus**](ResolverRuleAssociationStatus.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |



