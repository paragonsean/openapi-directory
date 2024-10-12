

# VpcIngressConnection

The App Runner resource that specifies an App Runner endpoint for incoming traffic. It establishes a connection between a VPC interface endpoint and a App Runner service, to make your App Runner service accessible from only within an Amazon VPC.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vpcIngressConnectionArn** | [**String**](String.md) |  |  [optional] |
|**vpcIngressConnectionName** | [**String**](String.md) |  |  [optional] |
|**serviceArn** | [**String**](String.md) |  |  [optional] |
|**status** | [**VpcIngressConnectionStatus**](VpcIngressConnectionStatus.md) |  |  [optional] |
|**accountId** | [**String**](String.md) |  |  [optional] |
|**domainName** | [**String**](String.md) |  |  [optional] |
|**ingressVpcConfiguration** | [**VpcIngressConnectionIngressVpcConfiguration**](VpcIngressConnectionIngressVpcConfiguration.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**deletedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



