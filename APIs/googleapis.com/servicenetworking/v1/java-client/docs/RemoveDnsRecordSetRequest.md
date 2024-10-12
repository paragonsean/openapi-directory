

# RemoveDnsRecordSetRequest

Request to remove a record set from a private managed DNS zone in the shared producer host project. The name, type, ttl, and data values must all exactly match an existing record set in the specified zone.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerNetwork** | **String** | Required. The network that the consumer is using to connect with services. Must be in the form of projects/{project}/global/networks/{network} {project} is the project number, as in &#39;12345&#39; {network} is the network name. |  [optional] |
|**dnsRecordSet** | [**DnsRecordSet**](DnsRecordSet.md) |  |  [optional] |
|**zone** | **String** | Required. The name of the private DNS zone in the shared producer host project from which the record set will be removed. |  [optional] |



