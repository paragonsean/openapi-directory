

# Host

<p>A resource that represents the infrastructure where a third-party provider is installed. The host is used when you create connections to an installed third-party provider type, such as GitHub Enterprise Server. You create one host for all connections to that provider.</p> <note> <p>A host created through the CLI or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by setting up the host in the console.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**hostArn** | [**String**](String.md) |  |  [optional] |
|**providerType** | [**ProviderType**](ProviderType.md) |  |  [optional] |
|**providerEndpoint** | [**String**](String.md) |  |  [optional] |
|**vpcConfiguration** | [**HostVpcConfiguration**](HostVpcConfiguration.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |



