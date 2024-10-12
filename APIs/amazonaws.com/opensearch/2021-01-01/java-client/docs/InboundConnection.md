

# InboundConnection

Describes an inbound cross-cluster connection for Amazon OpenSearch Service. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\">Cross-cluster search for Amazon OpenSearch Service</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localDomainInfo** | [**CreateOutboundConnectionResponseLocalDomainInfo**](CreateOutboundConnectionResponseLocalDomainInfo.md) |  |  [optional] |
|**remoteDomainInfo** | [**CreateOutboundConnectionResponseRemoteDomainInfo**](CreateOutboundConnectionResponseRemoteDomainInfo.md) |  |  [optional] |
|**connectionId** | [**String**](String.md) |  |  [optional] |
|**connectionStatus** | [**InboundConnectionConnectionStatus**](InboundConnectionConnectionStatus.md) |  |  [optional] |
|**connectionMode** | [**ConnectionMode**](ConnectionMode.md) |  |  [optional] |



