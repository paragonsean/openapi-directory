

# ResolverRule

For queries that originate in your VPC, detailed information about a Resolver rule, which specifies how to route DNS queries out of the VPC. The <code>ResolverRule</code> parameter appears in the response to a <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html\">CreateResolverRule</a>, <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverRule.html\">DeleteResolverRule</a>, <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRule.html\">GetResolverRule</a>, <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html\">ListResolverRules</a>, or <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverRule.html\">UpdateResolverRule</a> request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**creatorRequestId** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  [optional] |
|**domainName** | [**String**](String.md) |  |  [optional] |
|**status** | [**ResolverRuleStatus**](ResolverRuleStatus.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**ruleType** | [**RuleTypeOption**](RuleTypeOption.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**targetIps** | [**List**](List.md) |  |  [optional] |
|**resolverEndpointId** | [**String**](String.md) |  |  [optional] |
|**ownerId** | [**String**](String.md) |  |  [optional] |
|**shareStatus** | [**ShareStatus**](ShareStatus.md) |  |  [optional] |
|**creationTime** | [**String**](String.md) |  |  [optional] |
|**modificationTime** | [**String**](String.md) |  |  [optional] |



