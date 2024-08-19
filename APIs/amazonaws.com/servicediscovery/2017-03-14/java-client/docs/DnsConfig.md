

# DnsConfig

<p>A complex type that contains information about the Amazon Route 53 DNS records that you want Cloud Map to create when you register an instance.</p> <important> <p>The record types of a service can only be changed by deleting the service and recreating it with a new <code>Dnsconfig</code>.</p> </important>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namespaceId** | [**String**](String.md) |  |  [optional] |
|**routingPolicy** | [**RoutingPolicy**](RoutingPolicy.md) |  |  [optional] |
|**dnsRecords** | [**List**](List.md) |  |  |



