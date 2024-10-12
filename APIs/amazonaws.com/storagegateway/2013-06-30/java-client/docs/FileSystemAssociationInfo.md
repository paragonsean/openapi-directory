

# FileSystemAssociationInfo

Describes the object returned by <code>DescribeFileSystemAssociations</code> that describes a created file system association.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileSystemAssociationARN** | [**String**](String.md) |  |  [optional] |
|**locationARN** | [**String**](String.md) |  |  [optional] |
|**fileSystemAssociationStatus** | [**String**](String.md) |  |  [optional] |
|**auditDestinationARN** | [**String**](String.md) |  |  [optional] |
|**gatewayARN** | **String** | The Amazon Resource Name (ARN) of the gateway. Use the &lt;a&gt;ListGateways&lt;/a&gt; operation to return a list of gateways for your account and Amazon Web Services Region. |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**cacheAttributes** | [**CacheAttributes**](CacheAttributes.md) |  |  [optional] |
|**endpointNetworkConfiguration** | [**FileSystemAssociationInfoEndpointNetworkConfiguration**](FileSystemAssociationInfoEndpointNetworkConfiguration.md) |  |  [optional] |
|**fileSystemAssociationStatusDetails** | [**List**](List.md) |  |  [optional] |



