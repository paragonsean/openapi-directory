

# Connection

<p>A resource that is used to connect third-party source providers with services like CodePipeline.</p> <p>Note: A connection created through CloudFormation, the CLI, or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by updating the connection in the console.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionName** | [**String**](String.md) |  |  [optional] |
|**connectionArn** | [**String**](String.md) |  |  [optional] |
|**providerType** | [**ProviderType**](ProviderType.md) |  |  [optional] |
|**ownerAccountId** | [**String**](String.md) |  |  [optional] |
|**connectionStatus** | [**ConnectionStatus**](ConnectionStatus.md) |  |  [optional] |
|**hostArn** | [**String**](String.md) |  |  [optional] |



