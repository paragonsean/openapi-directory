

# NetworkConfig

Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableInterContainerTrafficEncryption** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableNetworkIsolation** | [**Boolean**](Boolean.md) |  |  [optional] |
|**vpcConfig** | [**VpcConfig**](VpcConfig.md) |  |  [optional] |



