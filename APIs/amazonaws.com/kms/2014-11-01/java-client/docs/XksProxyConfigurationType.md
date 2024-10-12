

# XksProxyConfigurationType

Detailed information about the external key store proxy (XKS proxy). Your external key store proxy translates KMS requests into a format that your external key manager can understand. These fields appear in a <a>DescribeCustomKeyStores</a> response only when the <code>CustomKeyStoreType</code> is <code>EXTERNAL_KEY_STORE</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectivity** | [**XksProxyConnectivityType**](XksProxyConnectivityType.md) |  |  [optional] |
|**accessKeyId** | [**String**](String.md) |  |  [optional] |
|**uriEndpoint** | [**String**](String.md) |  |  [optional] |
|**uriPath** | [**String**](String.md) |  |  [optional] |
|**vpcEndpointServiceName** | [**String**](String.md) |  |  [optional] |



