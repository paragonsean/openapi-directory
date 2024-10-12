# AwsStorageGateway.AssociateFileSystemInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userName** | **String** |  | 
**password** | **String** |  | 
**clientToken** | **String** |  | 
**gatewayARN** | **String** | The Amazon Resource Name (ARN) of the gateway. Use the &lt;a&gt;ListGateways&lt;/a&gt; operation to return a list of gateways for your account and Amazon Web Services Region. | 
**locationARN** | **String** |  | 
**tags** | **Array** |  | [optional] 
**auditDestinationARN** | **String** |  | [optional] 
**cacheAttributes** | [**CacheAttributes**](CacheAttributes.md) |  | [optional] 
**endpointNetworkConfiguration** | [**AssociateFileSystemInputEndpointNetworkConfiguration**](AssociateFileSystemInputEndpointNetworkConfiguration.md) |  | [optional] 


